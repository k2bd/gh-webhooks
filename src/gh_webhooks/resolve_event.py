import logging
from typing import Any, Dict, Optional, Type
from gh_webhooks.exceptions import NoMatchingModel

from gh_webhooks.types import (
    BranchProtectionRuleEvent,
    CheckRunEvent,
    CheckSuiteEvent,
    CodeScanningAlertEvent,
    CommitCommentEvent,
    CreateEvent,
    DeleteEvent,
    DeployKeyEvent,
    DeploymentEvent,
    DeploymentStatusEvent,
    DiscussionEvent,
    DiscussionCommentEvent,
    ForkEvent,
    GithubAppAuthorizationEvent,
    GollumEvent,
    InstallationEvent,
    InstallationRepositoriesEvent,
    IssueCommentEvent,
    IssuesEvent,
    LabelEvent,
    MarketplacePurchaseEvent,
    MemberEvent,
    MembershipEvent,
    MetaEvent,
    MilestoneEvent,
    Model,
    OrgBlockEvent,
    OrganizationEvent,
    PackageEvent,
    PageBuildEvent,
    PingEvent,
    ProjectEvent,
    ProjectCardEvent,
    ProjectColumnEvent,
    ProjectsV2ItemEvent,
    PublicEvent,
    PullRequestEvent,
    PullRequestReviewEvent,
    PullRequestReviewCommentEvent,
    PullRequestReviewThreadEvent,
    PushEvent,
    ReleaseEvent,
    RepositoryEvent,
    RepositoryDispatchEvent,
    RepositoryImportEvent,
    RepositoryVulnerabilityAlertEvent,
    SecretScanningAlertEvent,
    SecurityAdvisoryEvent,
    SponsorshipEvent,
    StarEvent,
    StatusEvent,
    TeamEvent,
    TeamAddEvent,
    WatchEvent,
    WorkflowDispatchEvent,
    WorkflowJobEvent,
    WorkflowRunEvent,
)

logger = logging.getLogger(__name__)

_cls_mapping = {
    "branch_protection_rule": BranchProtectionRuleEvent,
    "check_run": CheckRunEvent,
    "check_suite": CheckSuiteEvent,
    "code_scanning_alert": CodeScanningAlertEvent,
    "commit_comment": CommitCommentEvent,
    "create": CreateEvent,
    "delete": DeleteEvent,
    "deploy_key": DeployKeyEvent,
    "deployment": DeploymentEvent,
    "deployment_status": DeploymentStatusEvent,
    "discussion": DiscussionEvent,
    "discussion_comment": DiscussionCommentEvent,
    "fork": ForkEvent,
    "github_app_authorization": GithubAppAuthorizationEvent,
    "gollum": GollumEvent,
    "installation": InstallationEvent,
    "installation_repositories": InstallationRepositoriesEvent,
    "issue_comment": IssueCommentEvent,
    "issues": IssuesEvent,
    "label": LabelEvent,
    "marketplace_purchase": MarketplacePurchaseEvent,
    "member": MemberEvent,
    "membership": MembershipEvent,
    "meta": MetaEvent,
    "milestone": MilestoneEvent,
    "org_block": OrgBlockEvent,
    "organization": OrganizationEvent,
    "package": PackageEvent,
    "page_build": PageBuildEvent,
    "ping": PingEvent,
    "project": ProjectEvent,
    "project_card": ProjectCardEvent,
    "project_column": ProjectColumnEvent,
    "projects_v2_item": ProjectsV2ItemEvent,
    "public": PublicEvent,
    "pull_request": PullRequestEvent,
    "pull_request_review": PullRequestReviewEvent,
    "pull_request_review_comment": PullRequestReviewCommentEvent,
    "pull_request_review_thread": PullRequestReviewThreadEvent,
    "push": PushEvent,
    "release": ReleaseEvent,
    "repository": RepositoryEvent,
    "repository_dispatch": RepositoryDispatchEvent,
    "repository_import": RepositoryImportEvent,
    "repository_vulnerability_alert": RepositoryVulnerabilityAlertEvent,
    "secret_scanning_alert": SecretScanningAlertEvent,
    "security_advisory": SecurityAdvisoryEvent,
    "sponsorship": SponsorshipEvent,
    "star": StarEvent,
    "status": StatusEvent,
    "team": TeamEvent,
    "team_add": TeamAddEvent,
    "watch": WatchEvent,
    "workflow_dispatch": WorkflowDispatchEvent,
    "workflow_job": WorkflowJobEvent,
    "workflow_run": WorkflowRunEvent,
}


def _get_cls(kind: str) -> Type[Model]:
    # TODO: make this dynamic by constructing the event name and finding it
    cls = _cls_mapping.get(kind)
    if not kind:
        raise NoMatchingModel(f"No matching event kind")
    return cls


def resolve_event(event: Dict[str, Any], kind: str):
    """
    Try to match an event to a concrete model given the kind provided in the
    X-Github-Event header.

    Raises
    ------
    gh_webhooks.exceptions.NoMatchingModel
        If the event can't be matched to a model
    """
    cls = _get_cls(kind)
    logger.info(f"Matching event to {cls!r}")

    result = Model.parse_obj(event)
    while "__root__" in result.dict():
        result = result.__root__  # type: ignore
    return result
