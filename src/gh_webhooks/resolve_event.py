import logging
from typing import Any, Dict, Optional
from gh_webhooks.exceptions import NoMatchingModel

from gh_webhooks.types import (
    BranchProtectionRuleCreated,
    BranchProtectionRuleDeleted,
    BranchProtectionRuleEdited,
    CheckRunCompleted,
    CheckRunCreated,
    CheckRunRequestedAction,
    CheckRunRerequested,
    CheckSuiteCompleted,
    CheckSuiteRequested,
    CheckSuiteRerequested,
    CodeScanningAlertAppearedInBranch,
    CodeScanningAlertClosedByUser,
    CodeScanningAlertCreated,
    CodeScanningAlertFixed,
    CodeScanningAlertReopened,
    CommitCommentCreated,
    CreateEvent,
    DeleteEvent,
    DeployKeyCreated,
    DeployKeyDeleted,
    DeploymentCreated,
    DeploymentStatusCreated,
    DiscussionAnswered,
    DiscussionCategoryChanged,
    DiscussionCommentCreated,
    DiscussionCommentDeleted,
    DiscussionCommentEdited,
    DiscussionCreated,
    DiscussionDeleted,
    DiscussionEdited,
    DiscussionLabeled,
    DiscussionLocked,
    DiscussionPinned,
    DiscussionTransferred,
    DiscussionUnanswered,
    DiscussionUnlabeled,
    DiscussionUnlocked,
    DiscussionUnpinned,
    ForkEvent,
    GithubAppAuthorizationRevoked,
    GollumEvent,
    InstallationCreated,
    InstallationDeleted,
    InstallationNewPermissionsAccepted,
    InstallationRepositoriesAdded,
    InstallationRepositoriesRemoved,
    InstallationSuspend,
    InstallationUnsuspend,
    IssueCommentCreated,
    IssueCommentDeleted,
    IssueCommentEdited,
    IssuesAssigned,
    IssuesClosed,
    IssuesDeleted,
    IssuesDemilestoned,
    IssuesEdited,
    IssuesLabeled,
    IssuesLocked,
    IssuesMilestoned,
    IssuesOpened,
    IssuesPinned,
    IssuesReopened,
    IssuesTransferred,
    IssuesUnassigned,
    IssuesUnlabeled,
    IssuesUnlocked,
    IssuesUnpinned,
    LabelCreated,
    LabelDeleted,
    LabelEdited,
    MarketplacePurchaseCancelled,
    MarketplacePurchaseChanged,
    MarketplacePurchasePendingChange,
    MarketplacePurchasePendingChangeCancelled,
    MarketplacePurchasePurchased,
    MemberAdded,
    MemberEdited,
    MemberRemoved,
    MembershipAdded,
    MembershipRemoved,
    MetaDeleted,
    MilestoneClosed,
    MilestoneCreated,
    MilestoneDeleted,
    Model,
    OrgBlockBlocked,
    OrgBlockUnblocked,
    OrganizationDeleted,
    OrganizationMemberAdded,
    OrganizationMemberInvited,
    OrganizationMemberRemoved,
    OrganizationRenamed,
    PackagePublished,
    PackageUpdated,
    PageBuildEvent,
    PingEvent,
    ProjectCardConverted,
    ProjectCardCreated,
    ProjectCardDeleted,
    ProjectCardEdited,
    ProjectCardMoved,
    ProjectClosed,
    ProjectColumnCreated,
    ProjectColumnDeleted,
    ProjectColumnEdited,
    ProjectColumnMoved,
    ProjectCreated,
    ProjectDeleted,
    ProjectEdited,
    ProjectReopened,
    ProjectsV2ItemArchived,
    ProjectsV2ItemConverted,
    ProjectsV2ItemCreated,
    ProjectsV2ItemDeleted,
    ProjectsV2ItemEdited,
    ProjectsV2ItemReordered,
    ProjectsV2ItemRestored,
    PublicEvent,
    PullRequestAssigned,
    PullRequestAutoMergeDisabled,
    PullRequestAutoMergeEnabled,
    PullRequestClosed,
    PullRequestConvertedToDraft,
    PullRequestEdited,
    PullRequestLabeled,
    PullRequestLocked,
    PullRequestOpened,
    PullRequestReadyForReview,
    PullRequestReopened,
    PullRequestReviewCommentCreated,
    PullRequestReviewCommentDeleted,
    PullRequestReviewCommentEdited,
    PullRequestReviewDismissed,
    PullRequestReviewEdited,
    PullRequestReviewRequestRemoved,
    PullRequestReviewRequested,
    PullRequestReviewSubmitted,
    PullRequestReviewThreadResolved,
    PullRequestReviewThreadUnresolved,
    PullRequestSynchronize,
    PullRequestUnassigned,
    PullRequestUnlabeled,
    PullRequestUnlocked,
    PushEvent,
    ReleaseCreated,
    ReleaseDeleted,
    ReleaseEdited,
    ReleasePrereleased,
    ReleasePublished,
    ReleaseReleased,
    ReleaseUnpublished,
    RepositoryArchived,
    RepositoryCreated,
    RepositoryDeleted,
    RepositoryEdited,
    RepositoryPrivatized,
    RepositoryPublicized,
    RepositoryRenamed,
    RepositoryTransferred,
    RepositoryUnarchived,
)

logger = logging.getLogger(__name__)


def _find_match(event: Dict[str, Any]):
    action: Optional[str] = event.get("action")

    if "rule" in event:
        # Branch protection rule events
        if action == "created":
            return BranchProtectionRuleCreated
        if action == "edited":
            return BranchProtectionRuleEdited
        if action == "deleted":
            return BranchProtectionRuleDeleted
    if "deployment_status" in event:
        if action == "created":
            return DeploymentStatusCreated
    if "check_run" in event:
        # Check Run events
        if action == "completed":
            return CheckRunCompleted
        if action == "created":
            return CheckRunCreated
        if action == "requested_action":
            return CheckRunRequestedAction
        if action == "rerequested":
            return CheckRunRerequested
    if "check_suite" in event:
        # Check suite events
        if action == "completed":
            return CheckSuiteCompleted
        if action == "requested":
            return CheckSuiteRequested
        if action == "rerequested":
            return CheckSuiteRerequested
    if "alert" in event and "commit_oid" in event:
        # Code scanning alert events
        if action == "appeared_in_branch":
            return CodeScanningAlertAppearedInBranch
        if action == "closed_by_user":
            return CodeScanningAlertClosedByUser
        if action == "created":
            return CodeScanningAlertCreated
        if action == "fixed":
            return CodeScanningAlertFixed
        if action == "reopened":
            return CodeScanningAlertReopened
    if "comment" in event:
        if "issue" in event:
            # Issue comment events
            if action == "created":
                return IssueCommentCreated
            if action == "deleted":
                return IssueCommentDeleted
            if action == "edited":
                return IssueCommentEdited
        elif "pull_request" in event:
            # Pull request review comment events
            if action == "created":
                return PullRequestReviewCommentCreated
            if action == "deleted":
                return PullRequestReviewCommentDeleted
            if action == "edited":
                return PullRequestReviewCommentEdited
        elif "discussion" in event:
            # Discussion comment events
            if action == "created":
                return DiscussionCommentCreated
            if action == "deleted":
                return DiscussionCommentDeleted
            if action == "edited":
                return DiscussionCommentEdited
        else:
            # Commit comment created
            if action == "created":
                return CommitCommentCreated
    if action is None and "pusher_type" in event:
        # Branch/Tag create and delete events
        if "master_branch" in event:
            return CreateEvent
        else:
            return DeleteEvent
    if "key" in event:
        # Deploy key events
        if action == "created":
            return DeployKeyCreated
        if action == "deleted":
            return DeployKeyDeleted
    if "deployment" in event:
        if "deployment_status" in event:
            if action == "created":
                return DeploymentStatusCreated
        else:
            if action == "created":
                return DeploymentCreated
    if "discussion" in event:
        # Discussion event
        # Note that discussion comment events are handled earlier
        if action == "answered":
            return DiscussionAnswered
        if action == "category_changed":
            return DiscussionCategoryChanged
        if action == "created":
            return DiscussionCreated
        if action == "deleted":
            return DiscussionDeleted
        if action == "edited":
            return DiscussionEdited
        if action == "labeled":
            return DiscussionLabeled
        if action == "locked":
            return DiscussionLocked
        if action == "pinned":
            return DiscussionPinned
        if action == "transferred":
            return DiscussionTransferred
        if action == "unanswered":
            return DiscussionUnanswered
        if action == "unlabeled":
            return DiscussionUnlabeled
        if action == "unlocked":
            return DiscussionUnlocked
        if action == "unpinned":
            return DiscussionUnpinned
    if "requester" in event:
        # Installation and Installation Repository events
        if "repository_selection" in event:
            if action == "added":
                return InstallationRepositoriesAdded
            if action == "removed":
                return InstallationRepositoriesRemoved
        else:
            if action == "created":
                return InstallationCreated
            if action == "deleted":
                return InstallationDeleted
            if action == "new_permissions_accepted":
                return InstallationNewPermissionsAccepted
            if action == "suspend":
                return InstallationSuspend
            if action == "unsuspend":
                return InstallationUnsuspend
    if action is None and "forkee" in event:
        return ForkEvent
    if action is None and "pages" in event:
        return GollumEvent
    if "issue" in action:
        if action == "assigned":
            return IssuesAssigned
        if action == "closed":
            return IssuesClosed
        if action == "deleted":
            return IssuesDeleted
        if action == "demilestoned":
            return IssuesDemilestoned
        if action == "edited":
            return IssuesEdited
        if action == "labeled":
            return IssuesLabeled
        if action == "locked":
            return IssuesLocked
        if action == "milestoned":
            return IssuesMilestoned
        if action == "opened":
            return IssuesOpened
        if action == "pinned":
            return IssuesPinned
        if action == "reopened":
            return IssuesReopened
        if action == "transferred":
            return IssuesTransferred
        if action == "unassigned":
            return IssuesUnassigned
        if action == "unlabeled":
            return IssuesUnlabeled
        if action == "unlocked":
            return IssuesUnlocked
        if action == "unpinned":
            return IssuesUnpinned
    if "marketplace_purchase" in event:
        if action == "cancelled":
            return MarketplacePurchaseCancelled
        if action == "changed":
            return MarketplacePurchaseChanged
        if action == "pending_change":
            return MarketplacePurchasePendingChange
        if action == "pending_change_cancelled":
            return MarketplacePurchasePendingChangeCancelled
        if action == "purchased":
            return MarketplacePurchasePurchased
    if "member" in event:
        if "team" in event:
            if action == "added":
                return MembershipAdded
            if action == "removed":
                return MembershipRemoved
        else:
            if action == "added":
                return MemberAdded
            if action == "edited":
                return MemberEdited
            if action == "removed":
                return MemberRemoved
    if "hook" in event:
        if "zen" in event:
            return PingEvent
        else:
            return MetaDeleted
    if "milestone" in event:
        # Note: issue-related things handled earlier
        if action == "closed":
            return MilestoneClosed
        if action == "created":
            return MilestoneCreated
        if action == "deleted":
            return MilestoneDeleted
    if "membership" in event:
        if action == "deleted":
            return OrganizationDeleted
        if action == "member_added":
            return OrganizationMemberAdded
        if action == "member_removed":
            return OrganizationMemberRemoved
        if action == "renamed":
            return OrganizationRenamed
    if "blocked_user" in event:
        if action == "blocked":
            return OrgBlockBlocked
        if action == "unblocked":
            return OrgBlockUnblocked
    if "package" in event:
        if action == "published":
            return PackagePublished
        if action == "updated":
            return PackageUpdated
    if action is None and "build" in event:
        return PageBuildEvent
    if "project" in event:
        if action == "closed":
            return ProjectClosed
        if action == "created":
            return ProjectCreated
        if action == "deleted":
            return ProjectDeleted
        if action == "edited":
            return ProjectEdited
        if action == "reopened":
            return ProjectReopened
    if "project_card" in event:
        if action == "converted":
            return ProjectCardConverted
        if action == "created":
            return ProjectCardCreated
        if action == "deleted":
            return ProjectCardDeleted
        if action == "edited":
            return ProjectCardEdited
        if action == "moved":
            return ProjectCardMoved
    if "project_column" in event:
        if action == "created":
            return ProjectColumnCreated
        if action == "deleted":
            return ProjectColumnDeleted
        if action == "edited":
            return ProjectColumnEdited
        if action == "moved":
            return ProjectColumnMoved
    if "projects_v2_item" in event:
        if action == "archived":
            return ProjectsV2ItemArchived
        if action == "converted":
            return ProjectsV2ItemConverted
        if action == "created":
            return ProjectsV2ItemCreated
        if action == "deleted":
            return ProjectsV2ItemDeleted
        if action == "edited":
            return ProjectsV2ItemEdited
        if action == "reordered":
            return ProjectsV2ItemReordered
        if action == "restored":
            return ProjectsV2ItemRestored
    if "number" in event and "pull_request" in event:
        if action == "assigned": return PullRequestAssigned
        if action == "auto_merge_disabled": return PullRequestAutoMergeDisabled
        if action == "auto_merge_enabled": return PullRequestAutoMergeEnabled
        if action == "closed": return PullRequestClosed
        if action == "converted_to_draft": return PullRequestConvertedToDraft
        if action == "edited": return PullRequestEdited
        if action == "labeled": return PullRequestLabeled
        if action == "locked": return PullRequestLocked
        if action == "opened": return PullRequestOpened
        if action == "ready_for_review": return PullRequestReadyForReview
        if action == "reopened": return PullRequestReopened
        if action == "review_request_removed": return PullRequestReviewRequestRemoved
        if action == "review_requested": return PullRequestReviewRequested
        if action == "synchonize": return PullRequestSynchronize
        if action == "unassigned": return PullRequestUnassigned
        if action == "unlabeled": return PullRequestUnlabeled
        if action == "unlocked": return PullRequestUnlocked
    if "review" in action:
        if action == "dismissed": return PullRequestReviewDismissed
        if action == "edited": return PullRequestReviewEdited
        if action == "submitted": return PullRequestReviewSubmitted
    if "thread" in action:
        if action == "resolved": return PullRequestReviewThreadResolved
        if action == "unresolved": return PullRequestReviewThreadUnresolved
    if "pusher" in action:
        return PushEvent
    if "release" in action:
        if action == "created": return ReleaseCreated
        if action == "deleted": return ReleaseDeleted
        if action == "edited": return ReleaseEdited
        if action == "prereleased": return ReleasePrereleased
        if action == "published": return ReleasePublished
        if action == "released": return ReleaseReleased
        if action == "unpublished": return ReleaseUnpublished

    if "label" in event:
        # N.B. other label events handled earlier
        if action == "created":
            return LabelCreated
        if action == "deleted":
            return LabelDeleted
        if action == "edited":
            return LabelEdited
    if action == "member_invited":
        # Special-case
        return OrganizationMemberInvited
    if action == "revoked":
        # The only really notable thing about this event is action == 'revoked'
        return GithubAppAuthorizationRevoked
    if (
        "repository" in event
        and "sender" in event
        and "status" in event
        and "organization" in event
    ):
        # Repository import event
        # Difficult to determine this one
        
    if (
        "repository" in event
        and "sender" in event
        and "installation" in event
        and "organization" in event
    ):
        # General repository event
        # Difficult to determine this one
        if action == "created": return RepositoryCreated
        if action == "archived": return RepositoryArchived
        if action == "deleted": return RepositoryDeleted
        if action == "unarchived": return RepositoryUnarchived
        if action == "edited": return RepositoryEdited
        if action == "renamed": return RepositoryRenamed
        if action == "transferred": return RepositoryTransferred
        if action == "publicized": return RepositoryPublicized
        if action == "privatized": return RepositoryPrivatized
    if (
        "repository" in event
        and "sender" in event
        and "installation" in event
        and "organization" in event
        and action is None
    ):
        # Difficult to determine this one
        return PublicEvent

    raise NoMatchingModel(f"Could not parse event: {event}")


def resolve_event(event: Dict[str, Any]):
    """
    Try to match an event to a concrete model

    Raises
    ------
    gh_webhooks.exceptions.NoMatchingModel
        If the event can't be matched to a model
    """
    cls = _find_match(event)
    logger.info(f"Matching event to {cls!r}")

    result = Model.parse_obj(event)
    while "__root__" in result.dict():
        result = result.__root__  # type: ignore
    return result
