import ast
import os
import tempfile
from pathlib import Path

import astunparse
import requests
from datamodel_code_generator.__main__ import main as generate_main

ROOT = Path(__file__).parent.parent
CODEGEN_TARGET = str(ROOT / "src" / "gh_webhooks" / "types.py")
ALIASES = str(Path(__file__).parent / "aliases.json")

result = requests.get("https://unpkg.com/@octokit/webhooks-schemas/schema.json")

FORBID_STR = "extra = Extra.forbid"
PASS_STR = "pass"

with tempfile.TemporaryDirectory() as tempdir:
    schema_file = os.path.join(tempdir, "schema.json")
    with open(schema_file, "w") as f:
        f.write(result.text)

    generate_main(
        [
            "--input",
            schema_file,
            "--output",
            CODEGEN_TARGET,
            "--output-model-type",
            "pydantic_v2.BaseModel",
            "--disable-timestamp",
            "--allow-extra-fields",
            "--input-file-type",
            "jsonschema",
            "--target-python-version",
            "3.7",
            "--aliases",
            ALIASES,
            "--base-class",
            "gh_webhooks.base.GhWebhooksModel",
            "--enum-field-as-literal",
            "one",
            "--use-subclass-enum",
            "--reuse-model",
            "--force-optional",
        ]
    )

    class ReplaceBaseClass(ast.NodeTransformer):
        def visit_Module(self, node):
            rootmodel_imported = False
            for stmt in node.body:
                if isinstance(stmt, ast.ImportFrom) and stmt.module == "pydantic":
                    if any(alias.name == "RootModel" for alias in stmt.names):
                        # RootModel already imported
                        rootmodel_imported = True
                    else:
                        # Pydantic imported but not RootModel, so add it
                        stmt.names.append(ast.alias(name="RootModel", asname=None))
                        rootmodel_imported = True

            if not rootmodel_imported:
                # If RootModel is not imported yet, add the import statement
                node.body.insert(
                    0,
                    ast.ImportFrom(
                        module="pydantic",
                        names=[ast.alias(name="RootModel", asname=None)],
                        level=0,
                    ),
                )

            self.generic_visit(node)
            return node

        def visit_ClassDef(self, node):
            if any(
                name.id == "root"
                for name in ast.walk(node)
                if isinstance(name, ast.Name)
            ):
                node.bases = [
                    ast.Name(id="RootModel", ctx=ast.Load())
                    if base.id == "GhWebhooksModel"
                    else base
                    for base in node.bases
                ]
            return self.generic_visit(node)

    def update_root_model_classes(file_name):
        with open(file_name, "r") as f:
            tree = ast.parse(f.read())

        transformer = ReplaceBaseClass()
        transformed_tree = transformer.visit(tree)

        modified_code = astunparse.unparse(transformed_tree)

        with open(file_name, "w") as f:
            f.write(modified_code)

    update_root_model_classes(CODEGEN_TARGET)

    # Postprocessing
    def postprocess_content(content: str) -> str:
        return content.replace(FORBID_STR, PASS_STR)

    with open(CODEGEN_TARGET, "r") as f:
        generated_content = f.read()

    with open(CODEGEN_TARGET, "w") as f:
        f.write(postprocess_content(generated_content))
