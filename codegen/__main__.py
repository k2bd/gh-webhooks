import os
import tempfile
from pathlib import Path

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
            "--disable-timestamp",
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

    # Postprocessing
    def postprocess_content(content: str) -> str:
        return content.replace(FORBID_STR, PASS_STR)

    with open(CODEGEN_TARGET, "r") as f:
        generated_content = f.read()

    with open(CODEGEN_TARGET, "w") as f:
        f.write(postprocess_content(generated_content))
