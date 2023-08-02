from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, ConfigDict, Field, RootModel, confloat
from typing_extensions import Literal

from gh_webhooks.base import GhWebhooksModel


class Conclusion(Enum):
    success = "success"
    failure = "failure"
    neutral = "neutral"
    cancelled = "cancelled"
    timed_out = "timed_out"
    action_required = "action_required"
    stale = "stale"
    skipped = "skipped"
    NoneType_None = None


class Output(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    title: Optional[str] = None
    summary: Optional[str] = None
    text: Optional[str] = None
    annotations_count: Optional[int] = None
    annotations_url: Optional[AnyUrl] = None


class Status(str, Enum):
    in_progress = "in_progress"
    completed = "completed"
    queued = "queued"


class Conclusion1(Enum):
    success = "success"
    failure = "failure"
    neutral = "neutral"
    cancelled = "cancelled"
    timed_out = "timed_out"
    action_required = "action_required"
    stale = "stale"
    NoneType_None = None


class RequestedAction(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    identifier: Optional[str] = Field(
        None,
        description="The integrator reference of the action requested by the user.",
    )


class Status1(str, Enum):
    queued = "queued"
    in_progress = "in_progress"
    completed = "completed"
    waiting = "waiting"


class Status2(str, Enum):
    queued = "queued"
    in_progress = "in_progress"
    completed = "completed"


class Conclusion7(str, Enum):
    success = "success"
    failure = "failure"
    neutral = "neutral"
    cancelled = "cancelled"
    timed_out = "timed_out"
    action_required = "action_required"
    stale = "stale"


class Status5(Enum):
    requested = "requested"
    in_progress = "in_progress"
    completed = "completed"
    queued = "queued"
    NoneType_None = None


class State(str, Enum):
    open = "open"
    dismissed = "dismissed"
    fixed = "fixed"


class DismissedReason(Enum):
    false_positive = "false positive"
    won_t_fix = "won't fix"
    used_in_tests = "used in tests"
    NoneType_None = None


class Severity(Enum):
    none = "none"
    note = "note"
    warning = "warning"
    error = "error"
    NoneType_None = None


class Rule(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[str] = Field(
        None, description="A unique identifier for the rule used to detect the alert."
    )
    severity: Optional[Severity] = Field(None, description="The severity of the alert.")
    description: Optional[str] = Field(
        None, description="A short description of the rule used to detect the alert."
    )


class Tool(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[str] = Field(
        None,
        description="The name of the tool used to generate the code scanning analysis alert.",
    )
    version: Optional[str] = Field(
        None, description="The version of the tool used to detect the alert."
    )


class Rule1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[str] = Field(
        None, description="A unique identifier for the rule used to detect the alert."
    )
    severity: Optional[Severity] = Field(None, description="The severity of the alert.")
    description: Optional[str] = Field(
        None, description="A short description of the rule used to detect the alert."
    )
    name: Optional[str] = None
    full_description: Optional[str] = None
    tags: None = None
    help: None = None


class Tool1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[str] = Field(
        None,
        description="The name of the tool used to generate the code scanning analysis alert.",
    )
    version: Optional[str] = Field(
        None, description="The version of the tool used to detect the alert."
    )
    guid: Optional[str] = None


class State1(str, Enum):
    open = "open"
    dismissed = "dismissed"


class Rule2(Rule1):
    pass


class Rule3(Rule1):
    pass


class Rule4(Rule1):
    pass


class Rule5(Rule):
    pass


class Tool5(Tool):
    pass


class RefType(str, Enum):
    tag = "tag"
    branch = "branch"


class DismissedReason3(str, Enum):
    fix_started = "fix_started"
    inaccurate = "inaccurate"
    no_bandwidth = "no_bandwidth"
    not_used = "not_used"
    tolerable_risk = "tolerable_risk"


class Key(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    key: Optional[str] = None
    url: Optional[AnyUrl] = None
    title: Optional[str] = None
    verified: Optional[bool] = None
    created_at: Optional[datetime] = None
    read_only: Optional[bool] = None


class State4(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    success = "success"
    failure = "failure"
    error = "error"
    waiting = "waiting"
    queued = "queued"


class CheckRun4(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="The id of the check.")
    name: Optional[str] = Field(None, description="The name of the check run.")
    node_id: Optional[str] = None
    head_sha: Optional[str] = Field(
        None, description="The SHA of the commit that is being checked."
    )
    external_id: Optional[str] = None
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    details_url: Optional[AnyUrl] = None
    status: Optional[Status1] = Field(
        None,
        description="The current status of the check run. Can be `queued`, `in_progress`, or `completed`.",
    )
    conclusion: Optional[Conclusion] = Field(
        None,
        description="The result of the completed check run. Can be one of `success`, `failure`, `neutral`, `cancelled`, `timed_out`, `action_required` or `stale`. This value will be `null` until the check run has completed.",
    )
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class Category(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    is_answerable: Optional[Literal[True]] = None


class From(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    repository_id: Optional[int] = None
    emoji: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    slug: Optional[str] = None
    is_answerable: Optional[bool] = None


class Category1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[From] = Field(None, alias="from")


class Changes1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    category: Optional[Category1] = None


class State5(str, Enum):
    open = "open"
    converting = "converting"


class Title(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(None, alias="from")


class Body(Title):
    pass


class Changes2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    title: Optional[Title] = None
    body: Optional[Body] = None


class Category2(Category):
    pass


class Changes4(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    body: Optional[Body] = None


class Action(str, Enum):
    created = "created"
    edited = "edited"


class Page(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    page_name: Optional[str] = Field(None, description="The name of the page.")
    title: Optional[str] = Field(None, description="The current page title.")
    summary: None = None
    action: Optional[Action] = Field(
        None,
        description="The action that was performed on the page. Can be `created` or `edited`.",
    )
    sha: Optional[str] = Field(None, description="The latest commit SHA of the page.")
    html_url: Optional[AnyUrl] = Field(
        None, description="Points to the HTML wiki page."
    )


class Repository1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="Unique identifier of the repository")
    node_id: Optional[str] = None
    name: Optional[str] = Field(None, description="The name of the repository.")
    full_name: Optional[str] = None
    private: Optional[bool] = Field(
        None, description="Whether the repository is private or public."
    )


class RepositorySelection(str, Enum):
    all = "all"
    selected = "selected"


class RepositoriesAddedItem(Repository1):
    pass


class RepositoriesRemovedItem(Repository1):
    pass


class Login(Title):
    pass


class Slug(Title):
    pass


class Changes5(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    login: Optional[Login] = None
    slug: Optional[Slug] = None


class Type(str, Enum):
    Bot = "Bot"
    User = "User"
    Organization = "Organization"


class Account(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    avatar_url: Optional[AnyUrl] = None
    created_at: Optional[datetime] = None
    events_url: Optional[str] = None
    followers: Optional[int] = None
    followers_url: Optional[AnyUrl] = None
    following: Optional[int] = None
    following_url: Optional[str] = None
    gists_url: Optional[str] = None
    gravatar_id: Optional[str] = None
    has_organization_projects: Optional[bool] = None
    has_repository_projects: Optional[bool] = None
    hooks_url: Optional[str] = None
    html_url: Optional[AnyUrl] = None
    id: Optional[int] = None
    is_verified: Optional[bool] = None
    issues_url: Optional[str] = None
    login: Optional[str] = None
    members_url: Optional[str] = None
    name: Optional[str] = None
    node_id: Optional[str] = None
    organizations_url: Optional[AnyUrl] = None
    public_gists: Optional[int] = None
    public_members_url: Optional[str] = None
    public_repos: Optional[int] = None
    received_events_url: Optional[AnyUrl] = None
    repos_url: Optional[AnyUrl] = None
    site_admin: Optional[bool] = None
    slug: Optional[str] = None
    starred_url: Optional[str] = None
    subscriptions_url: Optional[AnyUrl] = None
    type: Optional[Type] = None
    updated_at: Optional[datetime] = None
    url: Optional[AnyUrl] = None


class State6(str, Enum):
    open = "open"
    closed = "closed"


class Body2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(
        None, alias="from", description="The previous version of the body."
    )


class Changes6(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    body: Optional[Body2] = None


class Title1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(
        None, alias="from", description="The previous version of the title."
    )


class Changes7(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    body: Optional[Body2] = None
    title: Optional[Title1] = None


class ActiveLockReason(Enum):
    resolved = "resolved"
    off_topic = "off-topic"
    too_heated = "too heated"
    spam = "spam"
    NoneType_None = None


class Color(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(
        None,
        alias="from",
        description="The previous version of the color if the action was `edited`.",
    )


class Name(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(
        None,
        alias="from",
        description="The previous version of the name if the action was `edited`.",
    )


class Description(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(
        None,
        alias="from",
        description="The previous version of the description if the action was `edited`.",
    )


class Changes10(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    color: Optional[Color] = None
    name: Optional[Name] = None
    description: Optional[Description] = None


class Sender(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    login: Optional[str] = None
    id: Optional[int] = None
    avatar_url: Optional[AnyUrl] = None
    gravatar_id: Optional[str] = None
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    followers_url: Optional[AnyUrl] = None
    following_url: Optional[str] = None
    gists_url: Optional[str] = None
    starred_url: Optional[str] = None
    subscriptions_url: Optional[AnyUrl] = None
    organizations_url: Optional[AnyUrl] = None
    repos_url: Optional[AnyUrl] = None
    events_url: Optional[str] = None
    received_events_url: Optional[AnyUrl] = None
    type: Optional[str] = None
    site_admin: Optional[bool] = None
    email: Optional[str] = None


class To(str, Enum):
    write = "write"
    admin = "admin"


class Permission(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    to: Optional[To] = None


class Changes11(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    permission: Optional[Permission] = None


class OldPermission(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(
        None,
        alias="from",
        description="The previous permissions of the collaborator if the action was edited.",
    )


class Changes12(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    old_permission: Optional[OldPermission] = None


class Scope(str, Enum):
    team = "team"
    organization = "organization"


class TeamItem(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    name: Optional[str] = None
    deleted: Optional[bool] = None


class Author(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[str] = None
    email: Optional[str] = None


class Committer(Author):
    pass


class HeadCommit(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[str] = None
    tree_id: Optional[str] = None
    message: Optional[str] = None
    timestamp: Optional[datetime] = None
    author: Optional[Author] = None
    committer: Optional[Committer] = None


class MergeGroup(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    head_sha: Optional[str] = Field(None, description="The SHA of the merge group.")
    head_ref: Optional[str] = Field(
        None, description="The full ref of the merge group."
    )
    base_ref: Optional[str] = Field(
        None,
        description="The full ref of the branch the merge group will be merged into.",
    )
    base_sha: Optional[str] = Field(
        None, description="The SHA of the merge group's parent commit."
    )
    head_commit: Optional[HeadCommit] = Field(
        None, description="An expanded representation of the `head_sha` commit."
    )


class ContentType(str, Enum):
    json = "json"
    form = "form"


class InsecureSsl(str, Enum):
    field_0 = "0"
    field_1 = "1"


class Config(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    content_type: Optional[ContentType] = Field(
        None,
        description="The media type used to serialize the payloads. Supported values include `json` and `form`. The default is `form`.",
    )
    secret: Optional[str] = Field(
        None,
        description="If provided, the `secret` will be used as the `key` to generate the HMAC hex digest value for [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers).",
    )
    url: Optional[AnyUrl] = Field(
        None, description="The URL to which the payloads will be delivered."
    )
    insecure_ssl: Optional[InsecureSsl] = Field(
        None,
        description="Determines whether the SSL certificate of the host for `url` will be verified when delivering payloads. Supported values include `0` (verification is performed) and `1` (verification is not performed). The default is `0`.",
    )


class DueOn(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(
        None,
        alias="from",
        description="The previous version of the due date if the action was `edited`.",
    )


class Title2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(
        None,
        alias="from",
        description="The previous version of the title if the action was `edited`.",
    )


class Changes13(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    description: Optional[Description] = None
    due_on: Optional[DueOn] = None
    title: Optional[Title2] = None


class Changes14(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    login: Optional[Login] = None


class PackageType(str, Enum):
    npm = "npm"
    maven = "maven"
    rubygems = "rubygems"
    docker = "docker"
    nuget = "nuget"
    CONTAINER = "CONTAINER"


class Info(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    type: Optional[str] = None
    oid: Optional[str] = None
    mode: Optional[int] = None
    name: Optional[str] = None
    path: Optional[str] = None
    size: Optional[int] = None
    collection: Optional[bool] = None


class Tag(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    digest: Optional[str] = None
    name: Optional[str] = None


class ContainerMetadatum(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    labels: Optional[Dict[(str, Any)]] = None
    manifest: Optional[Dict[(str, Any)]] = None
    tag: Optional[Tag] = None


class PackageFile(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    download_url: Optional[AnyUrl] = None
    id: Optional[int] = None
    name: Optional[str] = None
    sha256: Optional[str] = None
    sha1: Optional[str] = None
    md5: Optional[str] = None
    content_type: Optional[str] = None
    state: Optional[str] = None
    size: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Registry(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    about_url: Optional[AnyUrl] = None
    name: Optional[str] = None
    type: Optional[str] = None
    url: Optional[AnyUrl] = None
    vendor: Optional[str] = None


class ContainerMetadatum1(ContainerMetadatum):
    pass


class Error(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    message: Optional[str] = None


class Type1(str, Enum):
    Repository = "Repository"
    Organization = "Organization"
    App = "App"


class Config1(Config):
    pass


class LastResponse(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    code: None = None
    status: Optional[str] = None
    message: None = None


class Name1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(
        None,
        alias="from",
        description="The changes to the project if the action was `edited`.",
    )


class Body4(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(
        None,
        alias="from",
        description="The previous version of the body if the action was `edited`.",
    )


class Changes15(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[Name1] = None
    body: Optional[Body4] = None


class Note(Title):
    pass


class Changes16(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    note: Optional[Note] = None


class Changes17(Changes16):
    pass


class ColumnId(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[int] = Field(None, alias="from")


class Changes18(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    column_id: Optional[ColumnId] = None


class Name2(Title):
    pass


class Changes19(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[Name2] = None


class ArchivedAt(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: None = Field(None, alias="from")
    to: Optional[datetime] = None


class Changes20(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    archived_at: Optional[ArchivedAt] = None


class ContentType2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[Literal["DraftIssue"]] = Field(None, alias="from")
    to: Optional[Literal["Issue"]] = None


class Changes21(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    content_type: Optional[ContentType2] = None


class FieldType(str, Enum):
    single_select = "single_select"
    date = "date"
    number = "number"
    text = "text"
    iteration = "iteration"


class FieldValue(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    field_type: Optional[FieldType] = None
    field_node_id: Optional[str] = None


class Changes22(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    field_value: Optional[FieldValue] = None


class PreviousProjectsV2ItemNodeId(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(None, alias="from")
    to: Optional[str] = None


class Changes23(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    previous_projects_v2_item_node_id: Optional[PreviousProjectsV2ItemNodeId] = None


class ArchivedAt1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[datetime] = Field(None, alias="from")
    to: None = None


class Changes24(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    archived_at: Optional[ArchivedAt1] = None


class Ref(Title):
    pass


class Sha(Title):
    pass


class Base(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    ref: Optional[Ref] = None
    sha: Optional[Sha] = None


class Changes25(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    body: Optional[Body4] = None
    title: Optional[Title2] = None
    base: Optional[Base] = None


class Changes26(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    body: Optional[Body4] = None


class Body7(Body2):
    pass


class Changes27(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    body: Optional[Body7] = None


class Info2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    type: Optional[str] = None
    oid: Optional[str] = None
    mode: Optional[int] = None
    name: Optional[str] = None
    path: Optional[str] = None
    size: Optional[int] = None
    collection: Optional[bool] = None


class Label1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    description: Optional[str] = None
    source: Optional[AnyUrl] = None
    revision: Optional[str] = None
    image_url: Optional[AnyUrl] = None
    licenses: Optional[str] = None
    all_labels: Optional[Dict[(str, str)]] = None


class Config2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    digest: Optional[str] = None
    media_type: Optional[str] = None
    size: Optional[int] = None


class Layer(Config2):
    pass


class ManifestItem(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    digest: Optional[str] = None
    media_type: Optional[str] = None
    uri: Optional[str] = None
    size: Optional[int] = None
    config: Optional[Config2] = None
    layers: Optional[List[Layer]] = None


class ContainerMetadata(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    labels: Optional[Label1] = None
    manifest: Optional[ManifestItem] = None
    tag: Optional[Tag] = None


class Author1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    avatar_url: Optional[str] = None
    events_url: Optional[str] = None
    followers_url: Optional[str] = None
    following_url: Optional[str] = None
    gists_url: Optional[str] = None
    gravatar_id: Optional[str] = None
    html_url: Optional[str] = None
    id: Optional[int] = None
    login: Optional[str] = None
    node_id: Optional[str] = None
    organizations_url: Optional[str] = None
    received_events_url: Optional[str] = None
    repos_url: Optional[str] = None
    site_admin: Optional[bool] = None
    starred_url: Optional[str] = None
    subscriptions_url: Optional[str] = None
    type: Optional[str] = None
    url: Optional[str] = None


class ManifestItem1(ManifestItem):
    pass


class ContainerMetadata1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    labels: Optional[Label1] = None
    manifest: Optional[ManifestItem1] = None
    tag: Optional[Tag] = None


class Body8(Body4):
    pass


class Name3(Name):
    pass


class Changes28(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    body: Optional[Body8] = None
    name: Optional[Name3] = None


class Description2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(None, alias="from")


class DefaultBranch(Title):
    pass


class Homepage(Description2):
    pass


class Topics(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[List[str]] = Field(None, alias="from")


class Changes29(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    description: Optional[Description2] = None
    default_branch: Optional[DefaultBranch] = None
    homepage: Optional[Homepage] = None
    topics: Optional[Topics] = None


class Name4(Title):
    pass


class Repository14(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[Name4] = None


class Changes30(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    repository: Optional[Repository14] = None


class Status9(str, Enum):
    success = "success"
    cancelled = "cancelled"
    failure = "failure"


class Alert14(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    number: Optional[int] = None
    secret_type: Optional[str] = None
    resolution: None = None
    resolved_by: None = None
    resolved_at: None = None


class Resolution(str, Enum):
    false_positive = "false_positive"
    wont_fix = "wont_fix"
    revoked = "revoked"
    used_in_tests = "used_in_tests"


class Cvss(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    vector_string: Optional[str] = None
    score: Optional[float] = None


class Cwe(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    cwe_id: Optional[str] = None
    name: Optional[str] = None


class Identifier(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    value: Optional[str] = None
    type: Optional[str] = None


class Reference(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None


class Package2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    ecosystem: Optional[str] = None
    name: Optional[str] = None


class FirstPatchedVersion(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    identifier: Optional[str] = None


class Vulnerability(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    package: Optional[Package2] = None
    severity: Optional[str] = None
    vulnerable_version_range: Optional[str] = None
    first_patched_version: Optional[FirstPatchedVersion] = None


class SecurityAdvisory(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    cvss: Optional[Cvss] = None
    cwes: Optional[List[Cwe]] = None
    ghsa_id: Optional[str] = None
    cve_id: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    severity: Optional[str] = None
    identifiers: Optional[List[Identifier]] = None
    references: Optional[List[Reference]] = None
    published_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    withdrawn_at: Optional[datetime] = None
    vulnerabilities: Optional[List[Vulnerability]] = None


class SecurityAdvisoryPerformed(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["performed"]] = None
    security_advisory: Optional[SecurityAdvisory] = Field(
        None,
        description="The details of the security advisory, including summary, description, and severity.",
    )


class Vulnerability1(Vulnerability):
    pass


class SecurityAdvisory1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    cvss: Optional[Cvss] = None
    cwes: Optional[List[Cwe]] = None
    ghsa_id: Optional[str] = None
    cve_id: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    severity: Optional[str] = None
    identifiers: Optional[List[Identifier]] = None
    references: Optional[List[Reference]] = None
    published_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    withdrawn_at: Optional[datetime] = None
    vulnerabilities: Optional[List[Vulnerability1]] = None


class SecurityAdvisoryPublished(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["published"]] = None
    security_advisory: Optional[SecurityAdvisory1] = Field(
        None,
        description="The details of the security advisory, including summary, description, and severity.",
    )


class Vulnerability2(Vulnerability):
    pass


class SecurityAdvisory2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    cvss: Optional[Cvss] = None
    cwes: Optional[List[Cwe]] = None
    ghsa_id: Optional[str] = None
    cve_id: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    severity: Optional[str] = None
    identifiers: Optional[List[Identifier]] = None
    references: Optional[List[Reference]] = None
    published_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    withdrawn_at: Optional[datetime] = None
    vulnerabilities: Optional[List[Vulnerability2]] = None


class SecurityAdvisoryUpdated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["updated"]] = None
    security_advisory: Optional[SecurityAdvisory2] = Field(
        None,
        description="The details of the security advisory, including summary, description, and severity.",
    )


class Vulnerability3(Vulnerability):
    pass


class SecurityAdvisory3(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    cvss: Optional[Cvss] = None
    cwes: Optional[List[Cwe]] = None
    ghsa_id: Optional[str] = None
    cve_id: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    severity: Optional[str] = None
    identifiers: Optional[List[Identifier]] = None
    references: Optional[List[Reference]] = None
    published_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    withdrawn_at: Optional[datetime] = None
    vulnerabilities: Optional[List[Vulnerability3]] = None


class SecurityAdvisoryWithdrawn(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["withdrawn"]] = None
    security_advisory: Optional[SecurityAdvisory3] = Field(
        None,
        description="The details of the security advisory, including summary, description, and severity.",
    )


class SecurityAdvisoryEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                SecurityAdvisoryPerformed,
                SecurityAdvisoryPublished,
                SecurityAdvisoryUpdated,
                SecurityAdvisoryWithdrawn,
            )
        ]
    ] = None


class PrivacyLevel(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(
        None,
        alias="from",
        description="The `edited` event types include the details about the change when someone edits a sponsorship to change the privacy.",
    )


class Changes32(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    privacy_level: Optional[PrivacyLevel] = None


class State12(str, Enum):
    pending = "pending"
    success = "success"
    failure = "failure"
    error = "error"


class Tree(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    sha: Optional[str] = None
    url: Optional[AnyUrl] = None


class Reason(str, Enum):
    expired_key = "expired_key"
    not_signing_key = "not_signing_key"
    gpgverify_error = "gpgverify_error"
    gpgverify_unavailable = "gpgverify_unavailable"
    unsigned = "unsigned"
    unknown_signature_type = "unknown_signature_type"
    no_user = "no_user"
    unverified_email = "unverified_email"
    bad_email = "bad_email"
    unknown_key = "unknown_key"
    malformed_signature = "malformed_signature"
    invalid = "invalid"
    valid = "valid"


class Verification(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    verified: Optional[bool] = None
    reason: Optional[Reason] = None
    signature: Optional[str] = None
    payload: Optional[str] = None


class Parent(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    sha: Optional[str] = None
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None


class Commit3(Tree):
    pass


class Branch(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[str] = None
    commit: Optional[Commit3] = None
    protected: Optional[bool] = None


class Description3(Description):
    pass


class Name5(Name):
    pass


class Privacy(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[str] = Field(
        None,
        alias="from",
        description="The previous version of the team's privacy if the action was `edited`.",
    )


class From2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    admin: Optional[bool] = Field(
        None,
        description="The previous version of the team member's `admin` permission on a repository, if the action was `edited`.",
    )
    pull: Optional[bool] = Field(
        None,
        description="The previous version of the team member's `pull` permission on a repository, if the action was `edited`.",
    )
    push: Optional[bool] = Field(
        None,
        description="The previous version of the team member's `push` permission on a repository, if the action was `edited`.",
    )


class Permissions(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[From2] = Field(None, alias="from")


class Repository16(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    permissions: Optional[Permissions] = None


class Changes35(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    description: Optional[Description3] = None
    name: Optional[Name5] = None
    privacy: Optional[Privacy] = None
    repository: Optional[Repository16] = None


class Conclusion12(str, Enum):
    success = "success"
    failure = "failure"
    cancelled = "cancelled"
    skipped = "skipped"


class Status10(str, Enum):
    queued = "queued"
    in_progress = "in_progress"


class Status11(str, Enum):
    queued = "queued"
    waiting = "waiting"


class Conclusion13(str, Enum):
    success = "success"
    failure = "failure"
    neutral = "neutral"
    cancelled = "cancelled"
    timed_out = "timed_out"
    action_required = "action_required"
    stale = "stale"
    skipped = "skipped"


class Message(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    text: Optional[str] = None


class Location(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    path: Optional[str] = None
    start_line: Optional[int] = None
    end_line: Optional[int] = None
    start_column: Optional[int] = None
    end_column: Optional[int] = None


class AlertInstance(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    ref: Optional[str] = Field(
        None,
        description="The full Git reference, formatted as `refs/heads/<branch name>`.",
    )
    analysis_key: Optional[str] = Field(
        None,
        description="Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name.",
    )
    environment: Optional[str] = Field(
        None,
        description="Identifies the variable values associated with the environment in which the analysis that generated this alert instance was performed, such as the language that was analyzed.",
    )
    state: Optional[State] = Field(None, description="State of a code scanning alert.")
    commit_sha: Optional[str] = None
    message: Optional[Message] = None
    location: Optional[Location] = None
    classifications: Optional[List[str]] = None


class Actions(str, Enum):
    read = "read"
    write = "write"


class Permissions1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    actions: Optional[Actions] = None
    administration: Optional[Actions] = None
    blocking: Optional[Actions] = None
    checks: Optional[Actions] = None
    content_references: Optional[Actions] = None
    contents: Optional[Actions] = None
    deployments: Optional[Actions] = None
    discussions: Optional[Actions] = None
    emails: Optional[Actions] = None
    environments: Optional[Actions] = None
    followers: Optional[Actions] = None
    gpg_keys: Optional[Actions] = None
    interaction_limits: Optional[Actions] = None
    issues: Optional[Actions] = None
    keys: Optional[Actions] = None
    members: Optional[Actions] = None
    merge_queues: Optional[Actions] = None
    metadata: Optional[Actions] = None
    organization_administration: Optional[Actions] = None
    organization_hooks: Optional[Actions] = None
    organization_packages: Optional[Actions] = None
    organization_plan: Optional[Actions] = None
    organization_projects: Optional[Actions] = None
    organization_secrets: Optional[Actions] = None
    organization_self_hosted_runners: Optional[Actions] = None
    organization_user_blocking: Optional[Actions] = None
    packages: Optional[Actions] = None
    pages: Optional[Actions] = None
    plan: Optional[Actions] = None
    pull_requests: Optional[Actions] = None
    repository_hooks: Optional[Actions] = None
    repository_projects: Optional[Actions] = None
    secret_scanning_alerts: Optional[Actions] = None
    secrets: Optional[Actions] = None
    security_events: Optional[Actions] = None
    security_scanning_alert: Optional[Actions] = None
    single_file: Optional[Actions] = None
    starring: Optional[Actions] = None
    statuses: Optional[Actions] = None
    team_discussions: Optional[Actions] = None
    vulnerability_alerts: Optional[Actions] = None
    watching: Optional[Actions] = None
    workflows: Optional[Actions] = None


class Event(str, Enum):
    branch_protection_rule = "branch_protection_rule"
    check_run = "check_run"
    check_suite = "check_suite"
    code_scanning_alert = "code_scanning_alert"
    commit_comment = "commit_comment"
    create = "create"
    delete = "delete"
    dependabot_alert = "dependabot_alert"
    deployment = "deployment"
    deployment_protection_rule = "deployment_protection_rule"
    deployment_review = "deployment_review"
    deployment_status = "deployment_status"
    deploy_key = "deploy_key"
    discussion = "discussion"
    discussion_comment = "discussion_comment"
    fork = "fork"
    gollum = "gollum"
    issues = "issues"
    issue_comment = "issue_comment"
    label = "label"
    member = "member"
    membership = "membership"
    merge_group = "merge_group"
    merge_queue_entry = "merge_queue_entry"
    milestone = "milestone"
    organization = "organization"
    org_block = "org_block"
    page_build = "page_build"
    project = "project"
    projects_v2_item = "projects_v2_item"
    project_card = "project_card"
    project_column = "project_column"
    public = "public"
    pull_request = "pull_request"
    pull_request_review = "pull_request_review"
    pull_request_review_comment = "pull_request_review_comment"
    pull_request_review_thread = "pull_request_review_thread"
    push = "push"
    registry_package = "registry_package"
    release = "release"
    repository = "repository"
    repository_dispatch = "repository_dispatch"
    repository_ruleset = "repository_ruleset"
    secret_scanning_alert = "secret_scanning_alert"
    secret_scanning_alert_location = "secret_scanning_alert_location"
    security_and_analysis = "security_and_analysis"
    star = "star"
    status = "status"
    team = "team"
    team_add = "team_add"
    watch = "watch"
    workflow_dispatch = "workflow_dispatch"
    workflow_job = "workflow_job"
    workflow_run = "workflow_run"


class AuthorAssociation(str, Enum):
    COLLABORATOR = "COLLABORATOR"
    CONTRIBUTOR = "CONTRIBUTOR"
    FIRST_TIMER = "FIRST_TIMER"
    FIRST_TIME_CONTRIBUTOR = "FIRST_TIME_CONTRIBUTOR"
    MANNEQUIN = "MANNEQUIN"
    MEMBER = "MEMBER"
    NONE = "NONE"
    OWNER = "OWNER"


class MergeMethod(str, Enum):
    merge = "merge"
    squash = "squash"
    rebase = "rebase"


class BranchProtectionRuleArray(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[List[str]] = Field(None, title="Branch Protection Rule Array")


class BranchProtectionRuleBoolean(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[bool] = Field(None, title="Branch protection rule boolean")


class BranchProtectionRuleEnforcementLevel(str, Enum):
    off = "off"
    non_admins = "non_admins"
    everyone = "everyone"


class BranchProtectionRuleNumber(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[int] = Field(None, title="Branch protection rule number")


class BranchProtectionRule(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    repository_id: Optional[int] = None
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    pull_request_reviews_enforcement_level: Optional[
        BranchProtectionRuleEnforcementLevel
    ] = None
    required_approving_review_count: Optional[BranchProtectionRuleNumber] = None
    dismiss_stale_reviews_on_push: Optional[BranchProtectionRuleBoolean] = None
    require_code_owner_review: Optional[BranchProtectionRuleBoolean] = None
    authorized_dismissal_actors_only: Optional[BranchProtectionRuleBoolean] = None
    ignore_approvals_from_contributors: Optional[BranchProtectionRuleBoolean] = None
    require_last_push_approval: Optional[BranchProtectionRuleBoolean] = None
    required_status_checks: Optional[BranchProtectionRuleArray] = None
    required_status_checks_enforcement_level: Optional[
        BranchProtectionRuleEnforcementLevel
    ] = None
    strict_required_status_checks_policy: Optional[BranchProtectionRuleBoolean] = None
    signature_requirement_enforcement_level: Optional[
        BranchProtectionRuleEnforcementLevel
    ] = None
    linear_history_requirement_enforcement_level: Optional[
        BranchProtectionRuleEnforcementLevel
    ] = None
    admin_enforced: Optional[BranchProtectionRuleBoolean] = None
    create_protected: Optional[BranchProtectionRuleBoolean] = None
    allow_force_pushes_enforcement_level: Optional[
        BranchProtectionRuleEnforcementLevel
    ] = None
    allow_deletions_enforcement_level: Optional[
        BranchProtectionRuleEnforcementLevel
    ] = None
    merge_queue_enforcement_level: Optional[BranchProtectionRuleEnforcementLevel] = None
    required_deployments_enforcement_level: Optional[
        BranchProtectionRuleEnforcementLevel
    ] = None
    required_conversation_resolution_level: Optional[
        BranchProtectionRuleEnforcementLevel
    ] = None
    authorized_actors_only: Optional[BranchProtectionRuleBoolean] = None
    authorized_actor_names: Optional[BranchProtectionRuleArray] = None


class CheckRunDeployment(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    task: Optional[str] = None
    original_environment: Optional[str] = None
    environment: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    statuses_url: Optional[AnyUrl] = None
    repository_url: Optional[AnyUrl] = None


class CommitterModel(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[str] = Field(None, description="The git author's name.")
    email: Optional[str] = Field(None, description="The git author's email address.")
    date: Optional[datetime] = None
    username: Optional[str] = None


class DependabotAlertPackage(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[str] = Field(
        None, description="The unique package name within its ecosystem."
    )
    ecosystem: Optional[str] = Field(
        None, description="The package's language or package management ecosystem."
    )


class State14(str, Enum):
    dismissed = "dismissed"
    fixed = "fixed"
    open = "open"
    auto_dismissed = "auto_dismissed"


class Scope1(Enum):
    development = "development"
    runtime = "runtime"
    NoneType_None = None


class Dependency(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    package: Optional[DependabotAlertPackage] = None
    manifest_path: Optional[str] = Field(
        None,
        description="The full path to the dependency manifest file, relative to the root of the repository.",
    )
    scope: Optional[Scope1] = Field(
        None, description="The execution scope of the vulnerable dependency."
    )


class Severity6(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class FirstPatchedVersion4(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    identifier: Optional[str] = Field(
        None, description="The package version that patches this vulnerability."
    )


class Vulnerability4(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    package: Optional[DependabotAlertPackage] = None
    severity: Optional[Severity6] = Field(
        None, description="The severity of the vulnerability."
    )
    vulnerable_version_range: Optional[str] = Field(
        None,
        description="Conditions that identify vulnerable versions of this vulnerability's package.",
    )
    first_patched_version: Optional[FirstPatchedVersion4] = Field(
        None,
        description="Details pertaining to the package version that patches this vulnerability.",
    )


class Type2(str, Enum):
    CVE = "CVE"
    GHSA = "GHSA"


class Identifier4(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    type: Optional[Type2] = Field(None, description="The type of advisory identifier.")
    value: Optional[str] = Field(
        None, description="The value of the advisory identifer."
    )


class Reference4(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = Field(None, description="The URL of the reference.")


class SecurityVulnerability(Vulnerability4):
    pass


class DismissedReason4(Enum):
    fix_started = "fix_started"
    inaccurate = "inaccurate"
    no_bandwidth = "no_bandwidth"
    not_used = "not_used"
    tolerable_risk = "tolerable_risk"
    NoneType_None = None


class Status12(str, Enum):
    requested = "requested"
    in_progress = "in_progress"
    completed = "completed"
    queued = "queued"


class Category3(From):
    pass


class State15(str, Enum):
    open = "open"
    locked = "locked"
    converting = "converting"


class GithubOrg(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    login: str = "github"
    id: int = 9919
    node_id: str = "MDEyOk9yZ2FuaXphdGlvbjk5MTk="
    name: str = "GitHub"
    email: None = None
    avatar_url: AnyUrl = "https://avatars.githubusercontent.com/u/9919?v=4"
    gravatar_id: str = ""
    url: AnyUrl = "https://api.github.com/users/github"
    html_url: AnyUrl = "https://github.com/github"
    followers_url: AnyUrl = "https://api.github.com/users/github/followers"
    following_url: str = "https://api.github.com/users/github/following{/other_user}"
    gists_url: str = "https://api.github.com/users/github/gists{/gist_id}"
    starred_url: str = "https://api.github.com/users/github/starred{/owner}{/repo}"
    subscriptions_url: AnyUrl = "https://api.github.com/users/github/subscriptions"
    organizations_url: AnyUrl = "https://api.github.com/users/github/orgs"
    repos_url: AnyUrl = "https://api.github.com/users/github/repos"
    events_url: str = "https://api.github.com/users/github/events{/privacy}"
    received_events_url: AnyUrl = "https://api.github.com/users/github/received_events"
    type: str = "Organization"
    site_admin: bool = False


class InstallationLite(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="The ID of the installation.")
    node_id: Optional[str] = None


class TargetType(str, Enum):
    User = "User"
    Organization = "Organization"


class Permissions2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    actions: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token for GitHub Actions workflows, workflow runs, and artifacts.",
    )
    administration: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token for repository creation, deletion, settings, teams, and collaborators creation.",
    )
    blocking: Optional[Actions] = None
    checks: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token for checks on code.",
    )
    content_references: Optional[Actions] = None
    contents: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token for repository contents, commits, branches, downloads, releases, and merges.",
    )
    deployments: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token for deployments and deployment statuses.",
    )
    discussions: Optional[Actions] = None
    emails: Optional[Actions] = None
    environments: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token for managing repository environments.",
    )
    issues: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token for issues and related comments, assignees, labels, and milestones.",
    )
    members: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token for organization teams and members.",
    )
    merge_queues: Optional[Actions] = None
    metadata: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to search repositories, list collaborators, and access repository metadata.",
    )
    organization_administration: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to manage access to an organization.",
    )
    organization_events: Optional[Actions] = None
    organization_hooks: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to manage the post-receive hooks for an organization.",
    )
    organization_packages: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token for organization packages published to GitHub Packages.",
    )
    organization_plan: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token for viewing an organization's plan.",
    )
    organization_projects: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to manage organization projects and projects beta (where available).",
    )
    organization_secrets: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to manage organization secrets.",
    )
    organization_self_hosted_runners: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to view and manage GitHub Actions self-hosted runners available to an organization.",
    )
    organization_user_blocking: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to view and manage users blocked by the organization.",
    )
    packages: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token for packages published to GitHub Packages.",
    )
    pages: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds.",
    )
    pull_requests: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token for pull requests and related comments, assignees, labels, milestones, and merges.",
    )
    repository_hooks: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to manage the post-receive hooks for a repository.",
    )
    repository_projects: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to manage repository projects, columns, and cards.",
    )
    secret_scanning_alerts: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to view and manage secret scanning alerts.",
    )
    secrets: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to manage repository secrets.",
    )
    security_events: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to view and manage security events like code scanning alerts.",
    )
    security_scanning_alert: Optional[Actions] = None
    single_file: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to manage just a single file.",
    )
    statuses: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token for commit statuses.",
    )
    team_discussions: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to manage team discussions and related comments.",
    )
    vulnerability_alerts: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to manage Dependabot alerts.",
    )
    workflows: Optional[Actions] = Field(
        None,
        description="The level of permission granted to the access token to update GitHub Actions workflow files.",
    )


class Event1(str, Enum):
    branch_protection_rule = "branch_protection_rule"
    check_run = "check_run"
    check_suite = "check_suite"
    code_scanning_alert = "code_scanning_alert"
    commit_comment = "commit_comment"
    create = "create"
    delete = "delete"
    deployment = "deployment"
    deployment_review = "deployment_review"
    deployment_status = "deployment_status"
    deploy_key = "deploy_key"
    discussion = "discussion"
    discussion_comment = "discussion_comment"
    fork = "fork"
    gollum = "gollum"
    issues = "issues"
    issue_comment = "issue_comment"
    label = "label"
    member = "member"
    membership = "membership"
    merge_group = "merge_group"
    merge_queue_entry = "merge_queue_entry"
    milestone = "milestone"
    organization = "organization"
    org_block = "org_block"
    page_build = "page_build"
    project = "project"
    projects_v2_item = "projects_v2_item"
    project_card = "project_card"
    project_column = "project_column"
    public = "public"
    pull_request = "pull_request"
    pull_request_review = "pull_request_review"
    pull_request_review_comment = "pull_request_review_comment"
    pull_request_review_thread = "pull_request_review_thread"
    push = "push"
    registry_package = "registry_package"
    release = "release"
    repository = "repository"
    repository_dispatch = "repository_dispatch"
    secret_scanning_alert = "secret_scanning_alert"
    secret_scanning_alert_location = "secret_scanning_alert_location"
    security_and_analysis = "security_and_analysis"
    star = "star"
    status = "status"
    team = "team"
    team_add = "team_add"
    watch = "watch"
    workflow_dispatch = "workflow_dispatch"
    workflow_job = "workflow_job"
    workflow_run = "workflow_run"


class PullRequest11(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    diff_url: Optional[AnyUrl] = None
    patch_url: Optional[AnyUrl] = None
    merged_at: Optional[datetime] = None


class Label(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    node_id: Optional[str] = None
    url: Optional[AnyUrl] = Field(None, description="URL for the label")
    name: Optional[str] = Field(None, description="The name of the label.")
    description: Optional[str] = None
    color: Optional[str] = Field(
        None,
        description="6-character hex code, without the leading #, identifying the color",
    )
    default: Optional[bool] = None


class License(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    key: Optional[str] = None
    name: Optional[str] = None
    spdx_id: Optional[str] = None
    url: Optional[AnyUrl] = None
    node_id: Optional[str] = None


class Link(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    href: Optional[str] = None


class Account1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    type: Optional[str] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    login: Optional[str] = None
    organization_billing_email: Optional[str] = None


class Plan1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    monthly_price_in_cents: Optional[int] = None
    yearly_price_in_cents: Optional[int] = None
    price_model: Optional[str] = None
    has_free_trial: Optional[bool] = None
    unit_name: Optional[str] = None
    bullets: Optional[List[str]] = None


class MarketplacePurchase(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    account: Optional[Account1] = None
    billing_cycle: Optional[str] = None
    unit_count: Optional[int] = None
    on_free_trial: Optional[bool] = None
    free_trial_ends_on: Optional[datetime] = None
    next_billing_date: Optional[str] = None
    plan: Optional[Plan1] = None


class Organization(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    login: Optional[str] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    repos_url: Optional[AnyUrl] = None
    events_url: Optional[AnyUrl] = None
    hooks_url: Optional[AnyUrl] = None
    issues_url: Optional[AnyUrl] = None
    members_url: Optional[str] = None
    public_members_url: Optional[str] = None
    avatar_url: Optional[AnyUrl] = None
    description: Optional[str] = None


class PackageNpmMetadata(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[str] = None
    version: Optional[str] = None
    npm_user: Optional[str] = None
    author: Optional[Dict[(str, str)]] = None
    bugs: Optional[Dict[(str, str)]] = None
    dependencies: Optional[Dict[(str, str)]] = None
    dev_dependencies: Optional[Dict[(str, str)]] = None
    peer_dependencies: Optional[Dict[(str, str)]] = None
    optional_dependencies: Optional[Dict[(str, str)]] = None
    description: Optional[str] = None
    dist: Optional[Dict[(str, str)]] = None
    git_head: Optional[str] = None
    homepage: Optional[str] = None
    license: Optional[str] = None
    main: Optional[str] = None
    repository: Optional[Dict[(str, str)]] = None
    scripts: Optional[Dict[(str, Any)]] = None
    id: Optional[str] = None
    node_version: Optional[str] = None
    npm_version: Optional[str] = None
    has_shrinkwrap: Optional[bool] = None
    maintainers: Optional[List[Dict[(str, Any)]]] = None
    contributors: Optional[List[Dict[(str, Any)]]] = None
    engines: Optional[Dict[(str, str)]] = None
    keywords: Optional[List[str]] = None
    files: Optional[List[str]] = None
    bin: Optional[Dict[(str, Any)]] = None
    man: Optional[Dict[(str, Any)]] = None
    directories: Optional[Dict[(str, str)]] = None
    os: Optional[List[str]] = None
    cpu: Optional[List[str]] = None
    readme: Optional[str] = None
    installation_command: Optional[str] = None
    release_id: Optional[int] = None
    commit_oid: Optional[str] = None
    published_via_actions: Optional[bool] = None
    deleted_by_id: Optional[int] = None


class ValueItem(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[str] = None
    branch: Optional[str] = None
    commit: Optional[str] = None
    type: Optional[str] = None


class PackageNugetMetadata(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[Union[(str, int)]] = None
    name: Optional[str] = None
    value: Optional[Union[(bool, str, int, ValueItem)]] = None


class ProjectColumn(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    project_url: Optional[AnyUrl] = None
    cards_url: Optional[AnyUrl] = None
    id: Optional[int] = Field(
        None, description="The unique identifier of the project column"
    )
    node_id: Optional[str] = None
    name: Optional[str] = Field(None, description="Name of the project column")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ContentType3(str, Enum):
    DraftIssue = "DraftIssue"
    Issue = "Issue"
    PullRequest = "PullRequest"


class Links(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    self: Optional[Link] = None
    html: Optional[Link] = None
    pull_request: Optional[Link] = None


class StartSide(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    NoneType_None = None


class Side(str, Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class SubjectType(str, Enum):
    line = "line"
    file = "file"


class State19(str, Enum):
    commented = "commented"
    changes_requested = "changes_requested"
    approved = "approved"
    dismissed = "dismissed"


class Links4(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    html: Optional[Link] = None
    pull_request: Optional[Link] = None


class Links5(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    self: Optional[Link] = None
    html: Optional[Link] = None
    issue: Optional[Link] = None
    comments: Optional[Link] = None
    review_comments: Optional[Link] = None
    review_comment: Optional[Link] = None
    commits: Optional[Link] = None
    statuses: Optional[Link] = None


class Reactions(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    total_count: Optional[int] = None
    plus1: Optional[int] = Field(None, alias="+1")
    minus1: Optional[int] = Field(None, alias="-1")
    laugh: Optional[int] = None
    hooray: Optional[int] = None
    confused: Optional[int] = None
    heart: Optional[int] = None
    rocket: Optional[int] = None
    eyes: Optional[int] = None


class ReferencedWorkflow(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    path: Optional[str] = None
    sha: Optional[str] = None
    ref: Optional[str] = None


class RepoRef(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    url: Optional[AnyUrl] = None
    name: Optional[str] = None


class Visibility(str, Enum):
    public = "public"
    private = "private"
    internal = "internal"


class Permissions3(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    pull: Optional[bool] = None
    push: Optional[bool] = None
    admin: Optional[bool] = None
    maintain: Optional[bool] = None
    triage: Optional[bool] = None


class State22(str, Enum):
    open = "open"
    resolved = "resolved"


class Resolution1(Enum):
    false_positive = "false_positive"
    wont_fix = "wont_fix"
    revoked = "revoked"
    used_in_tests = "used_in_tests"
    NoneType_None = None


class Details(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    path: Optional[str] = Field(
        None,
        description="The file path in the repository",
        examples=["/example/secrets.txt"],
    )
    start_line: Optional[float] = Field(
        None, description="Line number at which the secret starts in the file"
    )
    end_line: Optional[float] = Field(
        None, description="Line number at which the secret ends in the file"
    )
    start_column: Optional[float] = Field(
        None,
        description="The column at which the secret starts within the start line when the file is interpreted as 8BIT ASCII",
    )
    end_column: Optional[float] = Field(
        None,
        description="The column at which the secret ends within the end line when the file is interpreted as 8BIT ASCII",
    )
    blob_sha: Optional[str] = Field(
        None,
        description="SHA-1 hash ID of the associated blob",
        examples=["af5626b4a114abcb82d63db7c8082c3c4756e51b"],
    )
    blob_url: Optional[str] = Field(
        None, description="The API URL to get the associated blob resource"
    )
    commit_sha: Optional[str] = Field(
        None,
        description="SHA-1 hash ID of the associated commit",
        examples=["af5626b4a114abcb82d63db7c8082c3c4756e51b"],
    )
    commit_url: Optional[str] = Field(
        None, description="The API URL to get the associated commit resource"
    )


class SecretScanningLocationItem(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    type: Optional[Literal["commit"]] = Field(
        None,
        description="The location type. Because secrets may be found in different types of resources (ie. code, comments, issues), this field identifies the type of resource where the secret was found.",
    )
    details: Optional[Details] = Field(
        None,
        description="Represents a 'commit' secret scanning location type. This location type shows that a secret was detected inside a commit to a repository.",
        title="Secret Scanning Location Commit",
    )


class Details1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    issue_title_url: Optional[AnyUrl] = Field(
        None,
        description="The API URL to get the issue where the secret was detected.",
        examples=["https://api.github.com/repos/octocat/Hello-World/issues/1347"],
    )


class SecretScanningLocationItem1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    type: Optional[Literal["issue_title"]] = Field(
        None,
        description="The location type. Because secrets may be found in different types of resources (ie. code, comments, issues), this field identifies the type of resource where the secret was found.",
    )
    details: Optional[Details1] = Field(
        None,
        description="Represents an 'issue_title' secret scanning location type. This location type shows that a secret was detected in the title of an issue.",
        title="Secret Scanning Location Issue Title",
    )


class Details2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    issue_body_url: Optional[AnyUrl] = Field(
        None,
        description="The API URL to get the issue where the secret was detected.",
        examples=["https://api.github.com/repos/octocat/Hello-World/issues/1347"],
    )


class SecretScanningLocationItem2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    type: Optional[Literal["issue_body"]] = Field(
        None,
        description="The location type. Because secrets may be found in different types of resources (ie. code, comments, issues), this field identifies the type of resource where the secret was found.",
    )
    details: Optional[Details2] = Field(
        None,
        description="Represents an 'issue_body' secret scanning location type. This location type shows that a secret was detected in the body of an issue.",
        title="Secret Scanning Location Issue Body",
    )


class Details3(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    issue_comment_url: Optional[AnyUrl] = Field(
        None,
        description="The API URL to get the issue comment where the secret was detected.",
        examples=[
            "https://api.github.com/repos/octocat/Hello-World/issues/comments/1081119451"
        ],
    )


class SecretScanningLocationItem3(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    type: Optional[Literal["issue_comment"]] = Field(
        None,
        description="The location type. Because secrets may be found in different types of resources (ie. code, comments, issues), this field identifies the type of resource where the secret was found.",
    )
    details: Optional[Details3] = Field(
        None,
        description="Represents an 'issue_comment' secret scanning location type. This location type shows that a secret was detected in a comment on an issue.",
        title="Secret Scanning Location Issue Comment",
    )


class SecretScanningLocation(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                SecretScanningLocationItem,
                SecretScanningLocationItem1,
                SecretScanningLocationItem2,
                SecretScanningLocationItem3,
            )
        ]
    ] = Field(None, title="Secret Scanning Location")


class SecurityAdvisoryCvss(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    score: Optional[confloat(ge=0.0, le=10.0)] = Field(
        None, description="The overall CVSS score of the advisory."
    )
    vector_string: Optional[str] = Field(
        None, description="The full CVSS vector string for the advisory."
    )


class SecurityAdvisoryCwes(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    cwe_id: Optional[str] = Field(None, description="The unique CWE ID.")
    name: Optional[str] = Field(
        None, description="The short, plain text name of the CWE."
    )


class SponsorshipTier(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    node_id: Optional[str] = None
    created_at: Optional[datetime] = None
    description: Optional[str] = None
    monthly_price_in_cents: Optional[int] = None
    monthly_price_in_dollars: Optional[int] = None
    name: Optional[str] = None
    is_one_time: Optional[bool] = None
    is_custom_ammount: Optional[bool] = None


class Privacy1(str, Enum):
    open = "open"
    closed = "closed"
    secret = "secret"


class NotificationSetting(str, Enum):
    notifications_enabled = "notifications_enabled"
    notifications_disabled = "notifications_disabled"


class Parent1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[str] = Field(None, description="Name of the team")
    id: Optional[int] = Field(None, description="Unique identifier of the team")
    node_id: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = Field(None, description="Description of the team")
    privacy: Optional[Privacy1] = None
    url: Optional[AnyUrl] = Field(None, description="URL for the team")
    html_url: Optional[AnyUrl] = None
    members_url: Optional[str] = None
    repositories_url: Optional[AnyUrl] = None
    permission: Optional[str] = Field(
        None, description="Permission that the team will have for its repositories"
    )
    notification_setting: Optional[NotificationSetting] = Field(
        None,
        description="Whether team members will receive notifications when their team is @mentioned",
    )


class Team(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[str] = Field(None, description="Name of the team")
    id: Optional[int] = Field(None, description="Unique identifier of the team")
    node_id: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = Field(None, description="Description of the team")
    privacy: Optional[Privacy1] = None
    url: Optional[AnyUrl] = Field(None, description="URL for the team")
    html_url: Optional[AnyUrl] = None
    members_url: Optional[str] = None
    repositories_url: Optional[AnyUrl] = None
    permission: Optional[str] = Field(
        None, description="Permission that the team will have for its repositories"
    )
    parent: Optional[Parent1] = None
    notification_setting: Optional[NotificationSetting] = Field(
        None,
        description="Whether team members will receive notifications when their team is @mentioned",
    )


class User(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    login: Optional[str] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    avatar_url: Optional[AnyUrl] = None
    gravatar_id: Optional[str] = None
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    followers_url: Optional[AnyUrl] = None
    following_url: Optional[str] = None
    gists_url: Optional[str] = None
    starred_url: Optional[str] = None
    subscriptions_url: Optional[AnyUrl] = None
    organizations_url: Optional[AnyUrl] = None
    repos_url: Optional[AnyUrl] = None
    events_url: Optional[str] = None
    received_events_url: Optional[AnyUrl] = None
    type: Optional[Type] = None
    site_admin: Optional[bool] = None


class WebhookEvent(str, Enum):
    branch_protection_rule = "branch_protection_rule"
    check_run = "check_run"
    check_suite = "check_suite"
    code_scanning_alert = "code_scanning_alert"
    commit_comment = "commit_comment"
    create = "create"
    delete = "delete"
    deployment = "deployment"
    deployment_status = "deployment_status"
    deploy_key = "deploy_key"
    discussion = "discussion"
    discussion_comment = "discussion_comment"
    fork = "fork"
    gollum = "gollum"
    issues = "issues"
    issue_comment = "issue_comment"
    label = "label"
    member = "member"
    membership = "membership"
    meta = "meta"
    milestone = "milestone"
    organization = "organization"
    org_block = "org_block"
    package = "package"
    page_build = "page_build"
    project = "project"
    projects_v2_item = "projects_v2_item"
    project_card = "project_card"
    project_column = "project_column"
    public = "public"
    pull_request = "pull_request"
    pull_request_review = "pull_request_review"
    pull_request_review_comment = "pull_request_review_comment"
    pull_request_review_thread = "pull_request_review_thread"
    push = "push"
    registry_package = "registry_package"
    release = "release"
    repository = "repository"
    repository_import = "repository_import"
    repository_vulnerability_alert = "repository_vulnerability_alert"
    secret_scanning_alert = "secret_scanning_alert"
    secret_scanning_alert_location = "secret_scanning_alert_location"
    security_and_analysis = "security_and_analysis"
    star = "star"
    status = "status"
    team = "team"
    team_add = "team_add"
    watch = "watch"
    workflow_job = "workflow_job"
    workflow_run = "workflow_run"


class WebhookEvents(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[Union[(List[WebhookEvent], List[str])]] = Field(
        None, title="Webhook Events"
    )


class Conclusion15(Enum):
    success = "success"
    failure = "failure"
    cancelled = "cancelled"
    skipped = "skipped"
    NoneType_None = None


class Head(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    ref: Optional[str] = None
    sha: Optional[str] = None
    repo: Optional[RepoRef] = None


class Base7(Head):
    pass


class PullRequest12(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    id: Optional[float] = None
    number: Optional[float] = None
    head: Optional[Head] = None
    base: Optional[Base7] = None


class Status14(str, Enum):
    requested = "requested"
    in_progress = "in_progress"
    completed = "completed"
    queued = "queued"
    waiting = "waiting"


class Conclusion17(str, Enum):
    failure = "failure"
    skipped = "skipped"
    success = "success"


class WorkflowStepCompleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[str] = None
    status: Optional[Literal["completed"]] = None
    conclusion: Optional[Conclusion17] = None
    number: Optional[int] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class WorkflowStepInProgress(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[str] = None
    status: Optional[Literal["in_progress"]] = None
    conclusion: None = None
    number: Optional[int] = None
    started_at: Optional[datetime] = None
    completed_at: None = None


class WorkflowStepQueued(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    name: Optional[str] = None
    status: Optional[Literal["queued"]] = None
    conclusion: None = None
    number: Optional[int] = None
    started_at: None = None
    completed_at: None = None


class WorkflowStep(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[(WorkflowStepInProgress, WorkflowStepQueued, WorkflowStepCompleted)]
    ] = Field(None, title="Workflow Step")


class Workflow(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    badge_url: Optional[AnyUrl] = None
    created_at: Optional[datetime] = None
    html_url: Optional[AnyUrl] = None
    id: Optional[int] = None
    name: Optional[str] = None
    node_id: Optional[str] = None
    path: Optional[str] = None
    state: Optional[str] = None
    updated_at: Optional[datetime] = None
    url: Optional[AnyUrl] = None


class AdminEnforced(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[BranchProtectionRuleBoolean] = Field(None, alias="from")


class AllowDeletionsEnforcementLevel(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[BranchProtectionRuleEnforcementLevel] = Field(None, alias="from")


class AllowForcePushesEnforcementLevel(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[BranchProtectionRuleEnforcementLevel] = Field(None, alias="from")


class AuthorizedActorsOnly(AdminEnforced):
    pass


class AuthorizedActorNames(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[BranchProtectionRuleArray] = Field(None, alias="from")


class AuthorizedDismissalActorsOnly(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[BranchProtectionRuleBoolean] = Field(None, alias="from")


class DismissStaleReviewsOnPush(AdminEnforced):
    pass


class PullRequestReviewsEnforcementLevel(AllowForcePushesEnforcementLevel):
    pass


class RequireCodeOwnerReview(AdminEnforced):
    pass


class RequiredApprovingReviewCount(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[BranchProtectionRuleNumber] = Field(None, alias="from")


class RequiredConversationResolutionLevel(AllowForcePushesEnforcementLevel):
    pass


class RequiredDeploymentsEnforcementLevel(AllowForcePushesEnforcementLevel):
    pass


class RequiredStatusChecks(AuthorizedActorNames):
    pass


class RequiredStatusChecksEnforcementLevel(AllowForcePushesEnforcementLevel):
    pass


class SignatureRequirementEnforcementLevel(AllowForcePushesEnforcementLevel):
    pass


class LinearHistoryRequirementEnforcementLevel(AllowForcePushesEnforcementLevel):
    pass


class Changes(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    admin_enforced: Optional[AdminEnforced] = None
    allow_deletions_enforcement_level: Optional[AllowDeletionsEnforcementLevel] = None
    allow_force_pushes_enforcement_level: Optional[
        AllowForcePushesEnforcementLevel
    ] = None
    authorized_actors_only: Optional[AuthorizedActorsOnly] = None
    authorized_actor_names: Optional[AuthorizedActorNames] = None
    authorized_dismissal_actors_only: Optional[AuthorizedDismissalActorsOnly] = None
    dismiss_stale_reviews_on_push: Optional[DismissStaleReviewsOnPush] = None
    pull_request_reviews_enforcement_level: Optional[
        PullRequestReviewsEnforcementLevel
    ] = None
    require_code_owner_review: Optional[RequireCodeOwnerReview] = None
    required_approving_review_count: Optional[RequiredApprovingReviewCount] = None
    required_conversation_resolution_level: Optional[
        RequiredConversationResolutionLevel
    ] = None
    required_deployments_enforcement_level: Optional[
        RequiredDeploymentsEnforcementLevel
    ] = None
    required_status_checks: Optional[RequiredStatusChecks] = None
    required_status_checks_enforcement_level: Optional[
        RequiredStatusChecksEnforcementLevel
    ] = None
    signature_requirement_enforcement_level: Optional[
        SignatureRequirementEnforcementLevel
    ] = None
    linear_history_requirement_enforcement_level: Optional[
        LinearHistoryRequirementEnforcementLevel
    ] = None


class Alert(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    number: Optional[int] = Field(None, description="The code scanning alert number.")
    created_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ.`",
    )
    url: Optional[AnyUrl] = Field(
        None, description="The REST API URL of the alert resource."
    )
    html_url: Optional[AnyUrl] = Field(
        None, description="The GitHub URL of the alert resource."
    )
    instances: Optional[List[AlertInstance]] = None
    most_recent_instance: Optional[AlertInstance] = None
    state: Optional[State] = Field(None, description="State of a code scanning alert.")
    dismissed_by: Optional[User] = None
    dismissed_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    dismissed_reason: Optional[DismissedReason] = Field(
        None,
        description="The reason for dismissing or closing the alert. Can be one of: `false positive`, `won't fix`, and `used in tests`.",
    )
    rule: Optional[Rule] = None
    tool: Optional[Tool] = None


class Instance(AlertInstance):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["dismissed"]] = None


class Alert1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    number: Optional[int] = Field(None, description="The code scanning alert number.")
    created_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ.`",
    )
    url: Optional[AnyUrl] = Field(
        None, description="The REST API URL of the alert resource."
    )
    html_url: Optional[AnyUrl] = Field(
        None, description="The GitHub URL of the alert resource."
    )
    instances: Optional[List[Instance]] = None
    most_recent_instance: Optional[AlertInstance] = None
    state: Optional[Literal["dismissed"]] = Field(
        None, description="State of a code scanning alert."
    )
    dismissed_by: Optional[User] = None
    dismissed_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    dismissed_reason: Optional[DismissedReason] = Field(
        None,
        description="The reason for dismissing or closing the alert. Can be one of: `false positive`, `won't fix`, and `used in tests`.",
    )
    rule: Optional[Rule1] = None
    tool: Optional[Tool1] = None


class Instance1(AlertInstance):
    model_config = ConfigDict(extra="allow")
    state: Optional[State1] = None


class Alert2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    number: Optional[int] = Field(None, description="The code scanning alert number.")
    created_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ.`",
    )
    url: Optional[AnyUrl] = Field(
        None, description="The REST API URL of the alert resource."
    )
    html_url: Optional[AnyUrl] = Field(
        None, description="The GitHub URL of the alert resource."
    )
    instances: Optional[List[Instance1]] = None
    most_recent_instance: Optional[AlertInstance] = None
    state: Optional[State1] = Field(None, description="State of a code scanning alert.")
    dismissed_by: None = None
    dismissed_at: None = Field(
        None,
        description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    dismissed_reason: None = Field(
        None,
        description="The reason for dismissing or closing the alert. Can be one of: `false positive`, `won't fix`, and `used in tests`.",
    )
    rule: Optional[Rule2] = None
    tool: Optional[Tool1] = None


class Instance2(AlertInstance):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["fixed"]] = None


class Alert3(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    number: Optional[int] = Field(None, description="The code scanning alert number.")
    created_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ.`",
    )
    url: Optional[AnyUrl] = Field(
        None, description="The REST API URL of the alert resource."
    )
    html_url: Optional[AnyUrl] = Field(
        None, description="The GitHub URL of the alert resource."
    )
    instances: Optional[List[Instance2]] = None
    state: Optional[Literal["fixed"]] = Field(
        None, description="State of a code scanning alert."
    )
    dismissed_by: Optional[User] = None
    dismissed_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    dismissed_reason: Optional[DismissedReason] = Field(
        None,
        description="The reason for dismissing or closing the alert. Can be one of: `false positive`, `won't fix`, and `used in tests`.",
    )
    rule: Optional[Rule3] = None
    tool: Optional[Tool1] = None
    most_recent_instance: Optional[AlertInstance] = None
    instances_url: Optional[AnyUrl] = None


class Instance3(AlertInstance):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["open"]] = None


class Alert4(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    number: Optional[int] = Field(None, description="The code scanning alert number.")
    created_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ.`",
    )
    url: Optional[AnyUrl] = Field(
        None, description="The REST API URL of the alert resource."
    )
    html_url: Optional[AnyUrl] = Field(
        None, description="The GitHub URL of the alert resource."
    )
    instances: Optional[List[Instance3]] = None
    most_recent_instance: Optional[AlertInstance] = None
    state: Optional[State] = Field(None, description="State of a code scanning alert.")
    dismissed_by: None = None
    dismissed_at: None = Field(
        None,
        description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    dismissed_reason: None = Field(
        None,
        description="The reason for dismissing or closing the alert. Can be one of: `false positive`, `won't fix`, and `used in tests`.",
    )
    rule: Optional[Rule4] = None
    tool: Optional[Tool1] = None


class Alert5(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    number: Optional[int] = Field(None, description="The code scanning alert number.")
    created_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ.`",
    )
    url: Optional[AnyUrl] = Field(
        None, description="The REST API URL of the alert resource."
    )
    html_url: Optional[AnyUrl] = Field(
        None, description="The GitHub URL of the alert resource."
    )
    instances: Optional[List[Instance3]] = None
    most_recent_instance: Optional[AlertInstance] = None
    state: Optional[Literal["open"]] = Field(
        None, description="State of a code scanning alert."
    )
    dismissed_by: None = None
    dismissed_at: None = Field(
        None,
        description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    dismissed_reason: None = Field(
        None,
        description="The reason for dismissing or closing the alert. Can be one of: `false positive`, `won't fix`, and `used in tests`.",
    )
    rule: Optional[Rule5] = None
    tool: Optional[Tool5] = None


class Comment(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    id: Optional[int] = Field(None, description="The ID of the commit comment.")
    node_id: Optional[str] = Field(
        None, description="The node ID of the commit comment."
    )
    user: Optional[User] = None
    position: Optional[int] = Field(
        None, description="The line index in the diff to which the comment applies."
    )
    line: Optional[int] = Field(
        None,
        description="The line of the blob to which the comment applies. The last line of the range for a multi-line comment",
    )
    path: Optional[str] = Field(
        None, description="The relative path of the file to which the comment applies."
    )
    commit_id: Optional[str] = Field(
        None, description="The SHA of the commit to which the comment applies."
    )
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    author_association: Optional[AuthorAssociation] = None
    body: Optional[str] = Field(None, description="The text of the comment.")


class Answer(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    node_id: Optional[str] = None
    html_url: Optional[str] = None
    parent_id: None = None
    child_comment_count: Optional[int] = None
    repository_url: Optional[str] = None
    discussion_id: Optional[int] = None
    author_association: Optional[AuthorAssociation] = None
    user: Optional[User] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    body: Optional[str] = None


class OldAnswer(Answer):
    pass


class Comment1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    node_id: Optional[str] = None
    html_url: Optional[str] = None
    parent_id: Optional[int] = None
    child_comment_count: Optional[int] = None
    repository_url: Optional[str] = None
    discussion_id: Optional[int] = None
    author_association: Optional[AuthorAssociation] = None
    user: Optional[User] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    body: Optional[str] = Field(None, description="The main text of the comment.")
    reactions: Optional[Reactions] = None


class GithubAppAuthorizationRevoked(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["revoked"]] = None
    sender: Optional[User] = None


class GithubAppAuthorizationEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[GithubAppAuthorizationRevoked] = None


class MarketplacePurchaseModel(MarketplacePurchase):
    model_config = ConfigDict(extra="allow")
    next_billing_date: Optional[datetime] = None


class MarketplacePurchaseCancelled(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["cancelled"]] = None
    effective_date: Optional[datetime] = None
    sender: Optional[Sender] = None
    marketplace_purchase: Optional[MarketplacePurchaseModel] = None
    previous_marketplace_purchase: Optional[MarketplacePurchase] = None


class MarketplacePurchaseChanged(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["changed"]] = None
    effective_date: Optional[datetime] = None
    sender: Optional[Sender] = None
    marketplace_purchase: Optional[MarketplacePurchaseModel] = None
    previous_marketplace_purchase: Optional[MarketplacePurchase] = None


class MarketplacePurchasePendingChange(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["pending_change"]] = None
    effective_date: Optional[datetime] = None
    sender: Optional[Sender] = None
    marketplace_purchase: Optional[MarketplacePurchaseModel] = None
    previous_marketplace_purchase: Optional[MarketplacePurchase] = None


class MarketplacePurchasePendingChangeCancelled(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["pending_change_cancelled"]] = None
    effective_date: Optional[datetime] = None
    sender: Optional[Sender] = None
    marketplace_purchase: Optional[MarketplacePurchaseModel] = None
    previous_marketplace_purchase: Optional[MarketplacePurchase] = None


class MarketplacePurchasePurchased(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["purchased"]] = None
    effective_date: Optional[datetime] = None
    sender: Optional[Sender] = None
    marketplace_purchase: Optional[MarketplacePurchaseModel] = None
    previous_marketplace_purchase: Optional[MarketplacePurchase] = None


class MarketplacePurchaseEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                MarketplacePurchaseCancelled,
                MarketplacePurchaseChanged,
                MarketplacePurchasePendingChange,
                MarketplacePurchasePendingChangeCancelled,
                MarketplacePurchasePurchased,
            )
        ]
    ] = None


class MembershipAdded(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["added"]] = None
    scope: Optional[Literal["team"]] = Field(
        None, description="The scope of the membership. Currently, can only be `team`."
    )
    member: Optional[User] = Field(
        None,
        description="The [user](https://docs.github.com/en/rest/reference/users) that was added or removed.",
    )
    sender: Optional[User] = None
    team: Optional[Team] = Field(
        None,
        description="The [team](https://docs.github.com/en/rest/reference/teams) for the membership.",
    )
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class MembershipRemoved(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["removed"]] = None
    scope: Optional[Scope] = Field(
        None, description="The scope of the membership. Currently, can only be `team`."
    )
    member: Optional[User] = Field(
        None,
        description="The [user](https://docs.github.com/en/rest/reference/users) that was added or removed.",
    )
    sender: Optional[User] = None
    team: Optional[Union[(Team, TeamItem)]] = Field(
        None,
        description="The [team](https://docs.github.com/en/rest/reference/teams) for the membership.",
    )
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class MembershipEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[Union[(MembershipAdded, MembershipRemoved)]] = None


class Hook(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    type: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    active: Optional[bool] = None
    events: Optional[WebhookEvents] = None
    config: Optional[Config] = Field(
        None, description="Configuration object of the webhook"
    )
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None


class OrgBlockBlocked(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["blocked"]] = None
    blocked_user: Optional[User] = Field(
        None, description="Information about the user that was blocked or unblocked."
    )
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class OrgBlockUnblocked(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unblocked"]] = None
    blocked_user: Optional[User] = Field(
        None, description="Information about the user that was blocked or unblocked."
    )
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class OrgBlockEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[Union[(OrgBlockBlocked, OrgBlockUnblocked)]] = None


class Invitation(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[float] = None
    node_id: Optional[str] = None
    login: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None
    created_at: Optional[datetime] = None
    failed_at: Optional[datetime] = None
    failed_reason: Optional[str] = None
    inviter: Optional[User] = None
    team_count: Optional[float] = None
    invitation_teams_url: Optional[AnyUrl] = None


class OrganizationMemberInvited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["member_invited"]] = None
    invitation: Optional[Invitation] = Field(
        None,
        description="The invitation for the user or email if the action is `member_invited`.",
    )
    user: Optional[User] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class OrganizationRenamed(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    changes: Optional[Changes14] = None
    action: Optional[Literal["renamed"]] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Release(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    id: Optional[int] = None
    tag_name: Optional[str] = None
    target_commitish: Optional[str] = None
    name: Optional[str] = None
    draft: Optional[bool] = None
    author: Optional[User] = None
    prerelease: Optional[bool] = None
    created_at: Optional[datetime] = None
    published_at: Optional[datetime] = None


class Build(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    status: Optional[str] = None
    error: Optional[Error] = None
    pusher: Optional[User] = None
    commit: Optional[str] = None
    duration: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Hook1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    type: Optional[Type1] = None
    id: Optional[int] = None
    name: Optional[str] = None
    active: Optional[bool] = None
    app_id: Optional[int] = Field(
        None,
        description="When you register a new GitHub App, GitHub sends a ping event to the **webhook URL** you specified during registration. The event contains the `app_id`, which is required for [authenticating](https://docs.github.com/en/apps/building-integrations/setting-up-and-registering-github-apps/about-authentication-options-for-github-apps) an app.",
    )
    events: Optional[WebhookEvents] = None
    config: Optional[Config1] = Field(
        None, description="Configuration object of the webhook"
    )
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    url: Optional[AnyUrl] = None
    test_url: Optional[AnyUrl] = None
    ping_url: Optional[AnyUrl] = None
    deliveries_url: Optional[AnyUrl] = None
    last_response: Optional[LastResponse] = None


class From1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    user: Optional[User] = None


class Owner(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[From1] = Field(None, alias="from")


class Changes31(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    owner: Optional[Owner] = None


class Sponsorship(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    node_id: Optional[str] = None
    created_at: Optional[datetime] = None
    sponsorable: Optional[User] = None
    sponsor: Optional[User] = None
    privacy_level: Optional[str] = None
    tier: Optional[SponsorshipTier] = None


class SponsorshipCancelled(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["cancelled"]] = None
    sponsorship: Optional[Sponsorship] = None
    sender: Optional[User] = None


class SponsorshipCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    sponsorship: Optional[Sponsorship] = None
    sender: Optional[User] = None


class SponsorshipEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    sponsorship: Optional[Sponsorship] = None
    changes: Optional[Changes32] = None
    sender: Optional[User] = None


class SponsorshipPendingCancellation(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["pending_cancellation"]] = None
    sponsorship: Optional[Sponsorship] = None
    effective_date: Optional[str] = Field(
        None,
        description="The `pending_cancellation` and `pending_tier_change` event types will include the date the cancellation or tier change will take effect.",
    )
    sender: Optional[User] = None


class Tier(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    from_: Optional[SponsorshipTier] = Field(None, alias="from")


class Changes33(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    tier: Optional[Tier] = None


class SponsorshipPendingTierChange(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["pending_tier_change"]] = None
    sponsorship: Optional[Sponsorship] = None
    effective_date: Optional[str] = Field(
        None,
        description="The `pending_cancellation` and `pending_tier_change` event types will include the date the cancellation or tier change will take effect.",
    )
    changes: Optional[Changes33] = None
    sender: Optional[User] = None


class Changes34(Changes33):
    pass


class SponsorshipTierChanged(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["tier_changed"]] = None
    sponsorship: Optional[Sponsorship] = None
    changes: Optional[Changes34] = None
    sender: Optional[User] = None


class SponsorshipEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                SponsorshipCancelled,
                SponsorshipCreated,
                SponsorshipEdited,
                SponsorshipPendingCancellation,
                SponsorshipPendingTierChange,
                SponsorshipTierChanged,
            )
        ]
    ] = None


class Author3(CommitterModel):
    model_config = ConfigDict(extra="allow")
    date: Optional[str] = None


class Committer1(Author3):
    pass


class Commit2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    author: Optional[Author3] = None
    committer: Optional[Committer1] = None
    message: Optional[str] = None
    tree: Optional[Tree] = None
    url: Optional[AnyUrl] = None
    comment_count: Optional[int] = None
    verification: Optional[Verification] = None


class Commit1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    sha: Optional[str] = None
    node_id: Optional[str] = None
    commit: Optional[Commit2] = None
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    comments_url: Optional[AnyUrl] = None
    author: Optional[User] = None
    committer: Optional[User] = None
    parents: Optional[List[Parent]] = None


class App(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="Unique identifier of the GitHub app")
    slug: Optional[str] = Field(None, description="The slug name of the GitHub app")
    node_id: Optional[str] = None
    owner: Optional[User] = None
    name: Optional[str] = Field(None, description="The name of the GitHub app")
    description: Optional[str] = None
    external_url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    permissions: Optional[Permissions1] = Field(
        None, description="The set of permissions for the GitHub app"
    )
    events: Optional[List[Event]] = Field(
        None, description="The list of events for the GitHub app"
    )


class AutoMerge(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    enabled_by: Optional[User] = None
    merge_method: Optional[MergeMethod] = Field(
        None, description="The merge method to use."
    )
    commit_title: Optional[str] = Field(
        None, description="Title for the merge commit message."
    )
    commit_message: Optional[str] = Field(
        None, description="Commit message for the merge commit."
    )


class CheckRunPullRequest(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    id: Optional[int] = None
    number: Optional[int] = None
    head: Optional[Head] = None
    base: Optional[Base7] = None


class CommitSimple(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[str] = None
    tree_id: Optional[str] = None
    message: Optional[str] = None
    timestamp: Optional[str] = None
    author: Optional[CommitterModel] = None
    committer: Optional[CommitterModel] = None


class Commit(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[str] = None
    tree_id: Optional[str] = None
    distinct: Optional[bool] = Field(
        None,
        description="Whether this commit is distinct from any that have been pushed before.",
    )
    message: Optional[str] = Field(None, description="The commit message.")
    timestamp: Optional[datetime] = Field(
        None, description="The ISO 8601 timestamp of the commit."
    )
    url: Optional[AnyUrl] = Field(
        None, description="URL that points to the commit API resource."
    )
    author: Optional[CommitterModel] = None
    committer: Optional[CommitterModel] = None
    added: Optional[List[str]] = Field(
        None,
        description="An array of files added in the commit. For extremely large commits where GitHub is unable to calculate this list in a timely manner, this may be empty even if files were added.",
    )
    modified: Optional[List[str]] = Field(
        None,
        description="An array of files modified by the commit. For extremely large commits where GitHub is unable to calculate this list in a timely manner, this may be empty even if files were modified.",
    )
    removed: Optional[List[str]] = Field(
        None,
        description="An array of files removed in the commit. For extremely large commits where GitHub is unable to calculate this list in a timely manner, this may be empty even if files were removed.",
    )


class SecurityAdvisory4(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    ghsa_id: Optional[str] = Field(
        None, description="Details for the GitHub Security Advisory."
    )
    cve_id: Optional[str] = Field(
        None, description="The unique CVE ID assigned to the advisory."
    )
    summary: Optional[str] = Field(
        None, description="A short, plain text summary of the advisory."
    )
    description: Optional[str] = Field(
        None, description="A long-form Markdown-supported description of the advisory."
    )
    vulnerabilities: Optional[List[Vulnerability4]] = Field(
        None, description="Vulnerable version range information for the advisory."
    )
    severity: Optional[Severity6] = Field(
        None, description="The severity of the advisory."
    )
    cvss: Optional[SecurityAdvisoryCvss] = None
    cwes: Optional[List[SecurityAdvisoryCwes]] = Field(
        None,
        description="Details for the advisory pertaining to Common Weakness Enumeration.",
    )
    identifiers: Optional[List[Identifier4]] = Field(
        None,
        description="Values that identify this advisory among security information sources.",
    )
    references: Optional[List[Reference4]] = Field(
        None, description="Links to additional advisory information."
    )
    published_at: Optional[datetime] = Field(
        None,
        description="The time that the advisory was published in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    updated_at: Optional[datetime] = Field(
        None,
        description="The time that the advisory was last modified in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    withdrawn_at: Optional[datetime] = Field(
        None,
        description="The time that the advisory was withdrawn in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )


class DependabotAlert(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    number: Optional[int] = Field(None, description="The security alert number.")
    state: Optional[State14] = Field(
        None, description="The state of the Dependabot alert."
    )
    dependency: Optional[Dependency] = Field(
        None, description="Details for the vulnerable dependency."
    )
    security_advisory: Optional[SecurityAdvisory4] = Field(
        None, description="Details for the GitHub Security Advisory."
    )
    security_vulnerability: Optional[SecurityVulnerability] = Field(
        None,
        description="Details pertaining to one vulnerable version range for the advisory.",
    )
    url: Optional[AnyUrl] = Field(
        None, description="The REST API URL of the alert resource."
    )
    html_url: Optional[AnyUrl] = Field(
        None, description="The GitHub URL of the alert resource."
    )
    created_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    updated_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    dismissed_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    auto_dismissed_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was auto-dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    dismissed_by: Optional[User] = None
    dismissed_reason: Optional[DismissedReason4] = Field(
        None, description="The reason that the alert was dismissed."
    )
    dismissed_comment: Optional[str] = Field(
        None, description="An optional comment associated with the alert's dismissal."
    )
    fixed_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )


class DeploymentWorkflowRun(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    name: Optional[str] = None
    path: Optional[str] = None
    display_title: Optional[str] = None
    node_id: Optional[str] = None
    head_branch: Optional[str] = None
    head_sha: Optional[str] = None
    run_number: Optional[int] = None
    event: Optional[str] = None
    status: Optional[Status12] = None
    conclusion: Optional[Conclusion1] = None
    workflow_id: Optional[int] = None
    check_suite_id: Optional[int] = None
    check_suite_node_id: Optional[str] = None
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    pull_requests: Optional[List[CheckRunPullRequest]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    actor: Optional[User] = None
    triggering_actor: Optional[User] = None
    run_attempt: Optional[int] = None
    run_started_at: Optional[datetime] = None
    referenced_workflows: Optional[List[ReferencedWorkflow]] = None


class Deployment(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    id: Optional[int] = Field(None, description="Unique identifier of the deployment")
    node_id: Optional[str] = None
    sha: Optional[str] = None
    ref: Optional[str] = Field(
        None, description="The ref to deploy. This can be a branch, tag, or sha."
    )
    task: Optional[str] = Field(
        None, description="Parameter to specify a task to execute"
    )
    payload: Optional[Dict[(str, Any)]] = None
    original_environment: Optional[str] = None
    environment: Optional[str] = Field(
        None, description="Name of the target deployment environment."
    )
    transient_environment: Optional[bool] = Field(
        None,
        description="Specifies if the given environment will no longer exist at some point in the future. Default: false.",
    )
    production_environment: Optional[bool] = Field(
        None,
        description="Specifies if the given environment is one that end-users directly interact with. Default: false.",
    )
    description: Optional[str] = None
    creator: Optional[User] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    statuses_url: Optional[AnyUrl] = None
    repository_url: Optional[AnyUrl] = None
    performed_via_github_app: Optional[App] = None


class Discussion(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    repository_url: Optional[str] = None
    category: Optional[Category3] = None
    answer_html_url: Optional[str] = None
    answer_chosen_at: Optional[datetime] = None
    answer_chosen_by: Optional[User] = None
    html_url: Optional[str] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    number: Optional[int] = None
    title: Optional[str] = Field(None, description="The discussion post's title.")
    user: Optional[User] = None
    state: Optional[State15] = None
    locked: Optional[bool] = None
    comments: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    author_association: Optional[AuthorAssociation] = None
    active_lock_reason: Optional[str] = None
    body: Optional[str] = Field(None, description="The discussion post's body text.")
    reactions: Optional[Reactions] = None


class Installation(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="The ID of the installation.")
    account: Optional[User] = None
    repository_selection: Optional[RepositorySelection] = Field(
        None,
        description="Describe whether all repositories have been selected or there's a selection involved",
    )
    access_tokens_url: Optional[AnyUrl] = None
    repositories_url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    app_id: Optional[int] = None
    app_slug: Optional[str] = None
    target_id: Optional[int] = Field(
        None,
        description="The ID of the user or organization this token is being scoped to.",
    )
    target_type: Optional[TargetType] = None
    permissions: Optional[Permissions2] = None
    events: Optional[List[Event1]] = None
    created_at: Optional[Union[(datetime, int)]] = None
    updated_at: Optional[Union[(datetime, int)]] = None
    single_file_name: Optional[str] = None
    has_multiple_single_files: Optional[bool] = None
    single_file_paths: Optional[List[str]] = None
    suspended_by: Optional[User] = None
    suspended_at: Optional[datetime] = None


class IssueComment(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = Field(None, description="URL for the issue comment")
    html_url: Optional[AnyUrl] = None
    issue_url: Optional[AnyUrl] = None
    id: Optional[int] = Field(
        None, description="Unique identifier of the issue comment"
    )
    node_id: Optional[str] = None
    user: Optional[User] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    author_association: Optional[AuthorAssociation] = None
    body: Optional[str] = Field(None, description="Contents of the issue comment")
    reactions: Optional[Reactions] = None
    performed_via_github_app: Optional[App] = None


class Membership(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    state: Optional[str] = Field(
        None, description="The state of the user's membership in the team."
    )
    role: Optional[str] = Field(None, description="The role of the user in the team.")
    organization_url: Optional[AnyUrl] = None
    user: Optional[User] = None


class Milestone(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    labels_url: Optional[AnyUrl] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    number: Optional[int] = Field(None, description="The number of the milestone.")
    title: Optional[str] = Field(None, description="The title of the milestone.")
    description: Optional[str] = None
    creator: Optional[User] = None
    open_issues: Optional[int] = None
    closed_issues: Optional[int] = None
    state: Optional[State6] = Field(None, description="The state of the milestone.")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    due_on: Optional[datetime] = None
    closed_at: Optional[datetime] = None


class ProjectCard(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    project_url: Optional[AnyUrl] = None
    column_url: Optional[AnyUrl] = None
    column_id: Optional[int] = None
    id: Optional[int] = Field(None, description="The project card's ID")
    node_id: Optional[str] = None
    note: Optional[str] = None
    archived: Optional[bool] = Field(
        None, description="Whether or not the card is archived"
    )
    creator: Optional[User] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    content_url: Optional[AnyUrl] = None
    after_id: Optional[Union[(str, float)]] = None


class Project(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    owner_url: Optional[AnyUrl] = None
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    columns_url: Optional[AnyUrl] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    name: Optional[str] = Field(None, description="Name of the project")
    body: Optional[str] = Field(None, description="Body of the project")
    number: Optional[int] = None
    state: Optional[State6] = Field(
        None, description="State of the project; either 'open' or 'closed'"
    )
    creator: Optional[User] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ProjectsV2Item(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[float] = None
    node_id: Optional[str] = None
    project_node_id: Optional[str] = None
    content_node_id: Optional[str] = None
    content_type: Optional[ContentType3] = None
    creator: Optional[User] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    archived_at: Optional[datetime] = None


class PullRequestReviewComment(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = Field(
        None, description="URL for the pull request review comment"
    )
    pull_request_review_id: Optional[int] = Field(
        None,
        description="The ID of the pull request review to which the comment belongs.",
    )
    id: Optional[int] = Field(
        None, description="The ID of the pull request review comment."
    )
    node_id: Optional[str] = Field(
        None, description="The node ID of the pull request review comment."
    )
    diff_hunk: Optional[str] = Field(
        None, description="The diff of the line that the comment refers to."
    )
    path: Optional[str] = Field(
        None, description="The relative path of the file to which the comment applies."
    )
    position: Optional[int] = Field(
        None, description="The line index in the diff to which the comment applies."
    )
    original_position: Optional[int] = Field(
        None,
        description="The index of the original line in the diff to which the comment applies.",
    )
    commit_id: Optional[str] = Field(
        None, description="The SHA of the commit to which the comment applies."
    )
    original_commit_id: Optional[str] = Field(
        None, description="The SHA of the original commit to which the comment applies."
    )
    user: Optional[User] = None
    body: Optional[str] = Field(None, description="The text of the comment.")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    html_url: Optional[AnyUrl] = Field(
        None, description="HTML URL for the pull request review comment."
    )
    pull_request_url: Optional[AnyUrl] = Field(
        None, description="URL for the pull request that the review comment belongs to."
    )
    author_association: Optional[AuthorAssociation] = None
    links: Optional[Links] = Field(None, alias="_links")
    reactions: Optional[Reactions] = None
    start_line: Optional[int] = Field(
        None, description="The first line of the range for a multi-line comment."
    )
    original_start_line: Optional[int] = Field(
        None, description="The first line of the range for a multi-line comment."
    )
    start_side: Optional[StartSide] = Field(
        "RIGHT",
        description="The side of the first line of the range for a multi-line comment.",
    )
    line: Optional[int] = Field(
        None,
        description="The line of the blob to which the comment applies. The last line of the range for a multi-line comment",
    )
    original_line: Optional[int] = Field(
        None,
        description="The line of the blob to which the comment applies. The last line of the range for a multi-line comment",
    )
    side: Optional[Side] = Field(
        None,
        description="The side of the first line of the range for a multi-line comment.",
    )
    in_reply_to_id: Optional[int] = Field(
        None, description="The comment ID to reply to."
    )
    subject_type: Optional[SubjectType] = Field(
        None,
        description="The level at which the comment is targeted, can be a diff line or a file.",
    )


class PullRequestReview(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="Unique identifier of the review")
    node_id: Optional[str] = None
    user: Optional[User] = None
    body: Optional[str] = Field(None, description="The text of the review.")
    commit_id: Optional[str] = Field(None, description="A commit SHA for the review.")
    submitted_at: Optional[datetime] = None
    state: Optional[State19] = None
    html_url: Optional[AnyUrl] = None
    pull_request_url: Optional[AnyUrl] = None
    author_association: Optional[AuthorAssociation] = None
    links: Optional[Links4] = Field(None, alias="_links")


class ReleaseAsset(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    browser_download_url: Optional[AnyUrl] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    name: Optional[str] = Field(None, description="The file name of the asset.")
    label: Optional[str] = None
    state: Optional[Literal["uploaded"]] = Field(
        None, description="State of the release asset."
    )
    content_type: Optional[str] = None
    size: Optional[int] = None
    download_count: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    uploader: Optional[User] = None


class ReleaseModel(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    assets_url: Optional[AnyUrl] = None
    upload_url: Optional[str] = None
    html_url: Optional[AnyUrl] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    tag_name: Optional[str] = Field(None, description="The name of the tag.")
    target_commitish: Optional[str] = Field(
        None,
        description="Specifies the commitish value that determines where the Git tag is created from.",
    )
    name: Optional[str] = None
    draft: Optional[bool] = Field(
        None, description="Wether the release is a draft or published"
    )
    author: Optional[User] = None
    prerelease: Optional[bool] = Field(
        None,
        description="Whether the release is identified as a prerelease or a full release.",
    )
    created_at: Optional[datetime] = None
    published_at: Optional[datetime] = None
    assets: Optional[List[ReleaseAsset]] = None
    tarball_url: Optional[AnyUrl] = None
    zipball_url: Optional[AnyUrl] = None
    body: Optional[str] = None
    mentions_count: Optional[int] = None
    reactions: Optional[Reactions] = None
    discussion_url: Optional[AnyUrl] = None


class RepositoryLite(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    archive_url: Optional[str] = Field(
        None,
        description="A template for the API URL to download the repository as an archive.",
    )
    assignees_url: Optional[str] = Field(
        None,
        description="A template for the API URL to list the available assignees for issues in the repository.",
    )
    blobs_url: Optional[str] = Field(
        None,
        description="A template for the API URL to create or retrieve a raw Git blob in the repository.",
    )
    branches_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about branches in the repository.",
    )
    collaborators_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about collaborators of the repository.",
    )
    comments_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about comments on the repository.",
    )
    commits_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about commits on the repository.",
    )
    compare_url: Optional[str] = Field(
        None, description="A template for the API URL to compare two commits or refs."
    )
    contents_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get the contents of the repository.",
    )
    contributors_url: Optional[AnyUrl] = Field(
        None,
        description="A template for the API URL to list the contributors to the repository.",
    )
    deployments_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the deployments of the repository."
    )
    description: Optional[str] = Field(None, description="The repository description.")
    downloads_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the downloads on the repository."
    )
    events_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the events of the repository."
    )
    fork: Optional[bool] = Field(None, description="Whether the repository is a fork.")
    forks_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the forks of the repository."
    )
    full_name: Optional[str] = Field(
        None, description="The full, globally unique, name of the repository."
    )
    git_commits_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about Git commits of the repository.",
    )
    git_refs_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about Git refs of the repository.",
    )
    git_tags_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about Git tags of the repository.",
    )
    hooks_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the hooks on the repository."
    )
    html_url: Optional[AnyUrl] = Field(
        None, description="The URL to view the repository on GitHub.com."
    )
    id: Optional[int] = Field(None, description="Unique identifier of the repository")
    issue_comment_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about issue comments on the repository.",
    )
    issue_events_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about issue events on the repository.",
    )
    issues_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about issues on the repository.",
    )
    keys_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about deploy keys on the repository.",
    )
    labels_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about labels of the repository.",
    )
    languages_url: Optional[AnyUrl] = Field(
        None,
        description="The API URL to get information about the languages of the repository.",
    )
    merges_url: Optional[AnyUrl] = Field(
        None, description="The API URL to merge branches in the repository."
    )
    milestones_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about milestones of the repository.",
    )
    name: Optional[str] = Field(None, description="The name of the repository.")
    node_id: Optional[str] = Field(
        None, description="The GraphQL identifier of the repository."
    )
    notifications_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about notifications on the repository.",
    )
    owner: Optional[User] = None
    private: Optional[bool] = Field(
        None, description="Whether the repository is private or public."
    )
    pulls_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about pull requests on the repository.",
    )
    releases_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about releases on the repository.",
    )
    stargazers_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the stargazers on the repository."
    )
    statuses_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about statuses of a commit.",
    )
    subscribers_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the subscribers on the repository."
    )
    subscription_url: Optional[AnyUrl] = Field(
        None,
        description="The API URL to subscribe to notifications for this repository.",
    )
    tags_url: Optional[AnyUrl] = Field(
        None, description="The API URL to get information about tags on the repository."
    )
    teams_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the teams on the repository."
    )
    trees_url: Optional[str] = Field(
        None,
        description="A template for the API URL to create or retrieve a raw Git tree of the repository.",
    )
    url: Optional[AnyUrl] = Field(
        None,
        description="The URL to get more information about the repository from the GitHub API.",
    )


class RepositoryVulnerabilityAlertAlert(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    number: Optional[int] = None
    node_id: Optional[str] = None
    state: Optional[State] = None
    affected_range: Optional[str] = None
    affected_package_name: Optional[str] = None
    dismisser: Optional[User] = None
    dismiss_reason: Optional[str] = None
    dismissed_at: Optional[datetime] = None
    severity: Optional[str] = None
    ghsa_id: Optional[str] = None
    external_reference: Optional[AnyUrl] = None
    external_identifier: Optional[str] = None
    fixed_in: Optional[str] = None
    fixed_at: Optional[datetime] = None
    fix_reason: Optional[str] = None
    created_at: Optional[datetime] = None


class Repository(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="Unique identifier of the repository")
    node_id: Optional[str] = Field(
        None, description="The GraphQL identifier of the repository."
    )
    name: Optional[str] = Field(None, description="The name of the repository.")
    full_name: Optional[str] = Field(
        None, description="The full, globally unique, name of the repository."
    )
    private: Optional[bool] = Field(
        None, description="Whether the repository is private or public."
    )
    owner: Optional[User] = None
    html_url: Optional[AnyUrl] = Field(
        None, description="The URL to view the repository on GitHub.com."
    )
    description: Optional[str] = Field(None, description="The repository description.")
    fork: Optional[bool] = Field(None, description="Whether the repository is a fork.")
    url: Optional[AnyUrl] = Field(
        None,
        description="The URL to get more information about the repository from the GitHub API.",
    )
    forks_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the forks of the repository."
    )
    keys_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about deploy keys on the repository.",
    )
    collaborators_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about collaborators of the repository.",
    )
    teams_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the teams on the repository."
    )
    hooks_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the hooks on the repository."
    )
    issue_events_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about issue events on the repository.",
    )
    events_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the events of the repository."
    )
    assignees_url: Optional[str] = Field(
        None,
        description="A template for the API URL to list the available assignees for issues in the repository.",
    )
    branches_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about branches in the repository.",
    )
    tags_url: Optional[AnyUrl] = Field(
        None, description="The API URL to get information about tags on the repository."
    )
    blobs_url: Optional[str] = Field(
        None,
        description="A template for the API URL to create or retrieve a raw Git blob in the repository.",
    )
    git_tags_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about Git tags of the repository.",
    )
    git_refs_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about Git refs of the repository.",
    )
    trees_url: Optional[str] = Field(
        None,
        description="A template for the API URL to create or retrieve a raw Git tree of the repository.",
    )
    statuses_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about statuses of a commit.",
    )
    languages_url: Optional[AnyUrl] = Field(
        None,
        description="The API URL to get information about the languages of the repository.",
    )
    stargazers_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the stargazers on the repository."
    )
    contributors_url: Optional[AnyUrl] = Field(
        None,
        description="A template for the API URL to list the contributors to the repository.",
    )
    subscribers_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the subscribers on the repository."
    )
    subscription_url: Optional[AnyUrl] = Field(
        None,
        description="The API URL to subscribe to notifications for this repository.",
    )
    commits_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about commits on the repository.",
    )
    git_commits_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about Git commits of the repository.",
    )
    comments_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about comments on the repository.",
    )
    issue_comment_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about issue comments on the repository.",
    )
    contents_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get the contents of the repository.",
    )
    compare_url: Optional[str] = Field(
        None, description="A template for the API URL to compare two commits or refs."
    )
    merges_url: Optional[AnyUrl] = Field(
        None, description="The API URL to merge branches in the repository."
    )
    archive_url: Optional[str] = Field(
        None,
        description="A template for the API URL to download the repository as an archive.",
    )
    downloads_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the downloads on the repository."
    )
    issues_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about issues on the repository.",
    )
    pulls_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about pull requests on the repository.",
    )
    milestones_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about milestones of the repository.",
    )
    notifications_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about notifications on the repository.",
    )
    labels_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about labels of the repository.",
    )
    releases_url: Optional[str] = Field(
        None,
        description="A template for the API URL to get information about releases on the repository.",
    )
    deployments_url: Optional[AnyUrl] = Field(
        None, description="The API URL to list the deployments of the repository."
    )
    created_at: Optional[Union[(int, datetime)]] = None
    updated_at: Optional[datetime] = None
    pushed_at: Optional[Union[(int, datetime)]] = None
    git_url: Optional[AnyUrl] = None
    ssh_url: Optional[str] = None
    clone_url: Optional[AnyUrl] = None
    svn_url: Optional[AnyUrl] = None
    homepage: Optional[str] = None
    size: Optional[int] = None
    stargazers_count: Optional[int] = None
    watchers_count: Optional[int] = None
    language: Optional[str] = None
    has_issues: Optional[bool] = Field(True, description="Whether issues are enabled.")
    has_projects: Optional[bool] = Field(
        True, description="Whether projects are enabled."
    )
    has_downloads: Optional[bool] = Field(
        True, description="Whether downloads are enabled."
    )
    has_wiki: Optional[bool] = Field(True, description="Whether the wiki is enabled.")
    has_pages: Optional[bool] = None
    has_discussions: Optional[bool] = Field(
        True, description="Whether discussions are enabled."
    )
    forks_count: Optional[int] = None
    mirror_url: Optional[AnyUrl] = None
    archived: Optional[bool] = Field(
        False, description="Whether the repository is archived."
    )
    disabled: Optional[bool] = Field(
        None, description="Returns whether or not this repository is disabled."
    )
    open_issues_count: Optional[int] = None
    license: Optional[License] = None
    forks: Optional[int] = None
    open_issues: Optional[int] = None
    watchers: Optional[int] = None
    stargazers: Optional[int] = None
    default_branch: Optional[str] = Field(
        None, description="The default branch of the repository."
    )
    allow_squash_merge: Optional[bool] = Field(
        True, description="Whether to allow squash merges for pull requests."
    )
    allow_merge_commit: Optional[bool] = Field(
        True, description="Whether to allow merge commits for pull requests."
    )
    allow_rebase_merge: Optional[bool] = Field(
        True, description="Whether to allow rebase merges for pull requests."
    )
    allow_auto_merge: Optional[bool] = Field(
        False, description="Whether to allow auto-merge for pull requests."
    )
    allow_forking: Optional[bool] = Field(
        None, description="Whether to allow private forks"
    )
    allow_update_branch: Optional[bool] = None
    use_squash_pr_title_as_default: Optional[bool] = None
    squash_merge_commit_message: Optional[str] = None
    squash_merge_commit_title: Optional[str] = None
    merge_commit_message: Optional[str] = None
    merge_commit_title: Optional[str] = None
    is_template: Optional[bool] = None
    web_commit_signoff_required: Optional[bool] = None
    topics: Optional[List[str]] = None
    visibility: Optional[Visibility] = None
    delete_branch_on_merge: Optional[bool] = Field(
        False,
        description="Whether to delete head branches when pull requests are merged",
    )
    master_branch: Optional[str] = None
    permissions: Optional[Permissions3] = None
    public: Optional[bool] = None
    organization: Optional[str] = None


class SecretScanningAlert(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    number: Optional[int] = Field(None, description="The security alert number.")
    created_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    updated_at: Optional[datetime] = None
    url: Optional[AnyUrl] = Field(
        None, description="The REST API URL of the alert resource."
    )
    html_url: Optional[AnyUrl] = Field(
        None, description="The GitHub URL of the alert resource."
    )
    locations_url: Optional[AnyUrl] = Field(
        None, description="The REST API URL of the code locations for this alert."
    )
    state: Optional[State22] = None
    resolution: Optional[Resolution1] = Field(
        None,
        description="**Required when the `state` is `resolved`.** The reason for resolving the alert.",
    )
    resolved_at: Optional[datetime] = Field(
        None,
        description="The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    resolved_by: Optional[User] = None
    resolution_comment: Optional[str] = Field(
        None, description="An optional comment to resolve an alert."
    )
    secret_type: Optional[str] = Field(
        None, description="The type of secret that secret scanning detected."
    )
    secret_type_display_name: Optional[str] = Field(
        None,
        description='User-friendly name for the detected secret, matching the `secret_type`.\nFor a list of built-in patterns, see "[Secret scanning patterns](https://docs.github.com/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)."',
    )
    secret: Optional[str] = Field(None, description="The secret that was detected.")
    push_protection_bypassed: Optional[bool] = Field(
        None,
        description="Whether push protection was bypassed for the detected secret.",
    )
    push_protection_bypassed_by: Optional[User] = None
    push_protection_bypassed_at: Optional[datetime] = Field(
        None,
        description="The time that push protection was bypassed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )


class Head5(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    label: Optional[str] = None
    ref: Optional[str] = None
    sha: Optional[str] = None
    user: Optional[User] = None
    repo: Optional[Repository] = None


class Base6(Head5):
    pass


class SimplePullRequest(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    html_url: Optional[AnyUrl] = None
    diff_url: Optional[AnyUrl] = None
    patch_url: Optional[AnyUrl] = None
    issue_url: Optional[AnyUrl] = None
    number: Optional[int] = None
    state: Optional[State6] = None
    locked: Optional[bool] = None
    title: Optional[str] = None
    user: Optional[User] = None
    body: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    merged_at: Optional[datetime] = None
    merge_commit_sha: Optional[str] = None
    assignee: Optional[User] = None
    assignees: Optional[List[User]] = None
    requested_reviewers: Optional[List[Union[(User, Team)]]] = None
    requested_teams: Optional[List[Team]] = None
    labels: Optional[List[Label]] = None
    milestone: Optional[Milestone] = None
    draft: Optional[bool] = None
    commits_url: Optional[AnyUrl] = None
    review_comments_url: Optional[AnyUrl] = None
    review_comment_url: Optional[str] = None
    comments_url: Optional[AnyUrl] = None
    statuses_url: Optional[AnyUrl] = None
    head: Optional[Head5] = None
    base: Optional[Base6] = None
    links: Optional[Links5] = Field(None, alias="_links")
    author_association: Optional[AuthorAssociation] = None
    auto_merge: Optional[AutoMerge] = None
    active_lock_reason: Optional[ActiveLockReason] = None


class WorkflowJob(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    run_id: Optional[float] = None
    run_attempt: Optional[int] = None
    run_url: Optional[AnyUrl] = None
    head_sha: Optional[str] = None
    node_id: Optional[str] = None
    name: Optional[str] = None
    check_run_url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    url: Optional[AnyUrl] = None
    status: Optional[Status1] = Field(
        None,
        description="The current status of the job. Can be `queued`, `in_progress`, or `completed`.",
    )
    steps: Optional[List[WorkflowStep]] = None
    conclusion: Optional[Conclusion15] = None
    labels: Optional[List[str]] = Field(
        None,
        description='Custom labels for the job. Specified by the [`"runs-on"` attribute](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idruns-on) in the workflow YAML.',
    )
    runner_id: Optional[int] = Field(
        None,
        description="The ID of the runner that is running this job. This will be `null` as long as `workflow_job[status]` is `queued`.",
    )
    runner_name: Optional[str] = Field(
        None,
        description="The name of the runner that is running this job. This will be `null` as long as `workflow_job[status]` is `queued`.",
    )
    runner_group_id: Optional[int] = Field(
        None,
        description="The ID of the runner group that is running this job. This will be `null` as long as `workflow_job[status]` is `queued`.",
    )
    runner_group_name: Optional[str] = Field(
        None,
        description="The name of the runner group that is running this job. This will be `null` as long as `workflow_job[status]` is `queued`.",
    )
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    workflow_name: Optional[str] = Field(None, description="The name of the workflow.")
    head_branch: Optional[str] = Field(
        None, description="The name of the current branch."
    )
    created_at: Optional[datetime] = None


class WorkflowRun(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    artifacts_url: Optional[AnyUrl] = Field(
        None, description="The URL to the artifacts for the workflow run."
    )
    cancel_url: Optional[AnyUrl] = Field(
        None, description="The URL to cancel the workflow run."
    )
    check_suite_url: Optional[AnyUrl] = Field(
        None, description="The URL to the associated check suite."
    )
    check_suite_id: Optional[int] = Field(
        None, description="The ID of the associated check suite."
    )
    check_suite_node_id: Optional[str] = Field(
        None, description="The node ID of the associated check suite."
    )
    conclusion: Optional[Conclusion] = None
    created_at: Optional[datetime] = None
    event: Optional[str] = None
    head_branch: Optional[str] = None
    head_commit: Optional[CommitSimple] = None
    head_repository: Optional[RepositoryLite] = None
    head_sha: Optional[str] = Field(
        None,
        description="The SHA of the head commit that points to the version of the workflow being run.",
    )
    path: Optional[str] = Field(None, description="The full path of the workflow")
    display_title: Optional[str] = None
    html_url: Optional[AnyUrl] = None
    id: Optional[int] = Field(None, description="The ID of the workflow run.")
    jobs_url: Optional[AnyUrl] = Field(
        None, description="The URL to the jobs for the workflow run."
    )
    logs_url: Optional[AnyUrl] = Field(
        None, description="The URL to download the logs for the workflow run."
    )
    node_id: Optional[str] = None
    name: Optional[str] = Field(None, description="The name of the workflow run.")
    pull_requests: Optional[List[PullRequest12]] = None
    repository: Optional[RepositoryLite] = None
    rerun_url: Optional[AnyUrl] = Field(
        None, description="The URL to rerun the workflow run."
    )
    run_number: Optional[int] = Field(
        None, description="The auto incrementing run number for the workflow run."
    )
    status: Optional[Status14] = None
    updated_at: Optional[datetime] = None
    url: Optional[AnyUrl] = Field(None, description="The URL to the workflow run.")
    workflow_id: Optional[int] = Field(
        None, description="The ID of the parent workflow."
    )
    workflow_url: Optional[AnyUrl] = Field(None, description="The URL to the workflow.")
    run_attempt: Optional[int] = Field(
        None,
        description="Attempt number of the run, 1 for first attempt and higher if the workflow was re-run.",
    )
    referenced_workflows: Optional[List[ReferencedWorkflow]] = None
    run_started_at: Optional[datetime] = Field(
        None, description="The start time of the latest run. Resets on re-run."
    )
    previous_attempt_url: Optional[AnyUrl] = Field(
        None,
        description="The URL to the previous attempted run of this workflow, if one exists.",
    )
    actor: Optional[User] = None
    triggering_actor: Optional[User] = None


class BranchProtectionRuleCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    rule: Optional[BranchProtectionRule] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class BranchProtectionRuleDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    rule: Optional[BranchProtectionRule] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class BranchProtectionRuleEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    rule: Optional[BranchProtectionRule] = None
    changes: Optional[Changes] = Field(
        None, description="If the action was `edited`, the changes to the rule."
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class BranchProtectionRuleEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                BranchProtectionRuleCreated,
                BranchProtectionRuleDeleted,
                BranchProtectionRuleEdited,
            )
        ]
    ] = None


class CheckSuite(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(
        None, description="The id of the check suite that this check run is part of."
    )
    node_id: Optional[str] = None
    head_branch: Optional[str] = None
    head_sha: Optional[str] = Field(
        None, description="The SHA of the head commit that is being checked."
    )
    status: Optional[Status] = None
    conclusion: Optional[Conclusion1] = None
    url: Optional[AnyUrl] = None
    before: Optional[str] = None
    after: Optional[str] = None
    pull_requests: Optional[List[CheckRunPullRequest]] = Field(
        None,
        description="An array of pull requests that match this check suite. A pull request matches a check suite if they have the same `head_branch`.  \n  \n**Note:**\n\n*   The `head_sha` of the check suite can differ from the `sha` of the pull request if subsequent pushes are made into the PR.\n*   When the check suite's `head_branch` is in a forked repository it will be `null` and the `pull_requests` array will be empty.",
    )
    deployment: Optional[CheckRunDeployment] = None
    app: Optional[App] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class CheckRun(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="The id of the check.")
    node_id: Optional[str] = None
    head_sha: Optional[str] = Field(
        None, description="The SHA of the commit that is being checked."
    )
    external_id: Optional[str] = None
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    details_url: Optional[AnyUrl] = None
    status: Optional[Literal["completed"]] = Field(
        None,
        description="The current status of the check run. Can be `queued`, `in_progress`, or `completed`.",
    )
    conclusion: Optional[Conclusion] = Field(
        None,
        description="The result of the completed check run. Can be one of `success`, `failure`, `neutral`, `cancelled`, `timed_out`, `action_required` or `stale`. This value will be `null` until the check run has completed.",
    )
    started_at: Optional[datetime] = Field(
        None,
        description="The time that the check run began. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    completed_at: Optional[datetime] = Field(
        None,
        description="The time the check completed. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    output: Optional[Output] = None
    name: Optional[str] = Field(None, description="The name of the check run.")
    check_suite: Optional[CheckSuite] = None
    app: Optional[App] = None
    pull_requests: Optional[List[CheckRunPullRequest]] = None
    deployment: Optional[CheckRunDeployment] = None


class CheckRunCompleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["completed"]] = None
    check_run: Optional[CheckRun] = Field(
        None,
        description="The [check_run](https://docs.github.com/en/rest/reference/checks#get-a-check-run).",
    )
    requested_action: Optional[RequestedAction] = Field(
        None, description="The action requested by the user."
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class CheckSuite1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(
        None, description="The id of the check suite that this check run is part of."
    )
    node_id: Optional[str] = None
    head_branch: Optional[str] = None
    head_sha: Optional[str] = Field(
        None, description="The SHA of the head commit that is being checked."
    )
    status: Optional[Status2] = None
    conclusion: Optional[Conclusion1] = None
    url: Optional[AnyUrl] = None
    before: Optional[str] = None
    after: Optional[str] = None
    pull_requests: Optional[List[CheckRunPullRequest]] = Field(
        None,
        description="An array of pull requests that match this check suite. A pull request matches a check suite if they have the same `head_branch`.  \n  \n**Note:**\n\n*   The `head_sha` of the check suite can differ from the `sha` of the pull request if subsequent pushes are made into the PR.\n*   When the check suite's `head_branch` is in a forked repository it will be `null` and the `pull_requests` array will be empty.",
    )
    deployment: Optional[CheckRunDeployment] = None
    app: Optional[App] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class CheckRun1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="The id of the check.")
    node_id: Optional[str] = None
    head_sha: Optional[str] = Field(
        None, description="The SHA of the commit that is being checked."
    )
    external_id: Optional[str] = None
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    details_url: Optional[AnyUrl] = None
    status: Optional[Status1] = Field(
        None,
        description="The current status of the check run. Can be `queued`, `in_progress`, or `completed`.",
    )
    conclusion: Optional[Conclusion] = Field(
        None,
        description="The result of the completed check run. Can be one of `success`, `failure`, `neutral`, `cancelled`, `timed_out`, `action_required` or `stale`. This value will be `null` until the check run has completed.",
    )
    started_at: Optional[datetime] = Field(
        None,
        description="The time that the check run began. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    completed_at: Optional[datetime] = Field(
        None,
        description="The time the check completed. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    output: Optional[Output] = None
    name: Optional[str] = Field(None, description="The name of the check run.")
    check_suite: Optional[CheckSuite1] = None
    app: Optional[App] = None
    pull_requests: Optional[List[CheckRunPullRequest]] = None
    deployment: Optional[CheckRunDeployment] = None


class CheckRunCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    check_run: Optional[CheckRun1] = Field(
        None,
        description="The [check_run](https://docs.github.com/en/rest/reference/checks#get-a-check-run).",
    )
    requested_action: Optional[RequestedAction] = Field(
        None, description="The action requested by the user."
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class CheckSuite2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(
        None, description="The id of the check suite that this check run is part of."
    )
    node_id: Optional[str] = None
    head_branch: Optional[str] = None
    head_sha: Optional[str] = Field(
        None, description="The SHA of the head commit that is being checked."
    )
    status: Optional[Status1] = None
    conclusion: Optional[Conclusion1] = None
    url: Optional[AnyUrl] = None
    before: Optional[str] = None
    after: Optional[str] = None
    pull_requests: Optional[List[CheckRunPullRequest]] = Field(
        None,
        description="An array of pull requests that match this check suite. A pull request matches a check suite if they have the same `head_branch`.  \n  \n**Note:**\n\n*   The `head_sha` of the check suite can differ from the `sha` of the pull request if subsequent pushes are made into the PR.\n*   When the check suite's `head_branch` is in a forked repository it will be `null` and the `pull_requests` array will be empty.",
    )
    deployment: Optional[CheckRunDeployment] = None
    app: Optional[App] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class CheckRun2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="The id of the check.")
    node_id: Optional[str] = None
    head_sha: Optional[str] = Field(
        None, description="The SHA of the commit that is being checked."
    )
    external_id: Optional[str] = None
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    details_url: Optional[AnyUrl] = None
    status: Optional[Status2] = Field(
        None,
        description="The current status of the check run. Can be `queued`, `in_progress`, or `completed`.",
    )
    conclusion: Optional[Conclusion] = Field(
        None,
        description="The result of the completed check run. Can be one of `success`, `failure`, `neutral`, `cancelled`, `timed_out`, `action_required` or `stale`. This value will be `null` until the check run has completed.",
    )
    started_at: Optional[datetime] = Field(
        None,
        description="The time that the check run began. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    completed_at: Optional[datetime] = Field(
        None,
        description="The time the check completed. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    output: Optional[Output] = None
    name: Optional[str] = Field(None, description="The name of the check run.")
    check_suite: Optional[CheckSuite2] = None
    app: Optional[App] = None
    pull_requests: Optional[List[CheckRunPullRequest]] = None
    deployment: Optional[CheckRunDeployment] = None


class CheckRunRequestedAction(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["requested_action"]] = None
    check_run: Optional[CheckRun2] = Field(
        None,
        description="The [check_run](https://docs.github.com/en/rest/reference/checks#get-a-check-run).",
    )
    requested_action: Optional[RequestedAction] = Field(
        None, description="The action requested by the user."
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class CheckSuite3(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(
        None, description="The id of the check suite that this check run is part of."
    )
    node_id: Optional[str] = None
    head_branch: Optional[str] = None
    head_sha: Optional[str] = Field(
        None, description="The SHA of the head commit that is being checked."
    )
    status: Optional[Literal["completed"]] = None
    conclusion: Optional[Conclusion7] = None
    url: Optional[AnyUrl] = None
    before: Optional[str] = None
    after: Optional[str] = None
    pull_requests: Optional[List[CheckRunPullRequest]] = Field(
        None,
        description="An array of pull requests that match this check suite. A pull request matches a check suite if they have the same `head_branch`.  \n  \n**Note:**\n\n*   The `head_sha` of the check suite can differ from the `sha` of the pull request if subsequent pushes are made into the PR.\n*   When the check suite's `head_branch` is in a forked repository it will be `null` and the `pull_requests` array will be empty.",
    )
    deployment: Optional[CheckRunDeployment] = None
    app: Optional[App] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class CheckRun3(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="The id of the check.")
    node_id: Optional[str] = None
    head_sha: Optional[str] = Field(
        None, description="The SHA of the commit that is being checked."
    )
    external_id: Optional[str] = None
    url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    details_url: Optional[AnyUrl] = None
    status: Optional[Literal["completed"]] = Field(
        None, description="The phase of the lifecycle that the check is currently in."
    )
    conclusion: Optional[Conclusion] = Field(
        None,
        description="The result of the completed check run. Can be one of `success`, `failure`, `neutral`, `cancelled`, `timed_out`, `action_required` or `stale`. This value will be `null` until the check run has `completed`.",
    )
    started_at: Optional[datetime] = Field(
        None,
        description="The time that the check run began. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    completed_at: Optional[datetime] = Field(
        None,
        description="The time the check completed. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.",
    )
    output: Optional[Output] = None
    name: Optional[str] = Field(None, description="The name of the check.")
    check_suite: Optional[CheckSuite3] = None
    app: Optional[App] = None
    pull_requests: Optional[List[CheckRunPullRequest]] = None
    deployment: Optional[CheckRunDeployment] = None


class CheckRunRerequested(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["rerequested"]] = None
    check_run: Optional[CheckRun3] = Field(
        None,
        description="The [check_run](https://docs.github.com/en/rest/reference/checks#get-a-check-run).",
    )
    requested_action: Optional[RequestedAction] = Field(
        None, description="The action requested by the user."
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class CheckRunEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                CheckRunCompleted,
                CheckRunCreated,
                CheckRunRequestedAction,
                CheckRunRerequested,
            )
        ]
    ] = None


class CheckSuite4(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    node_id: Optional[str] = None
    head_branch: Optional[str] = Field(
        None, description="The head branch name the changes are on."
    )
    head_sha: Optional[str] = Field(
        None, description="The SHA of the head commit that is being checked."
    )
    status: Optional[Status5] = Field(
        None,
        description="The summary status for all check runs that are part of the check suite. Can be `queued`, `requested`, `in_progress`, or `completed`.",
    )
    conclusion: Optional[Conclusion1] = Field(
        None,
        description="The summary conclusion for all check runs that are part of the check suite. Can be one of `success`, `failure`, `neutral`, `cancelled`, `timed_out`, `action_required` or `stale`. This value will be `null` until the check run has `completed`.",
    )
    url: Optional[AnyUrl] = Field(
        None, description="URL that points to the check suite API resource."
    )
    before: Optional[str] = None
    after: Optional[str] = None
    pull_requests: Optional[List[CheckRunPullRequest]] = Field(
        None,
        description="An array of pull requests that match this check suite. A pull request matches a check suite if they have the same `head_sha` and `head_branch`. When the check suite's `head_branch` is in a forked repository it will be `null` and the `pull_requests` array will be empty.",
    )
    app: Optional[App] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    runs_rerequestable: Optional[bool] = None
    rerequestable: Optional[bool] = None
    latest_check_runs_count: Optional[int] = None
    check_runs_url: Optional[AnyUrl] = None
    head_commit: Optional[CommitSimple] = None


class CheckSuiteCompleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["completed"]] = None
    check_suite: Optional[CheckSuite4] = Field(
        None,
        description="The [check_suite](https://docs.github.com/en/rest/reference/checks#suites).",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class CheckSuite5(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    node_id: Optional[str] = None
    head_branch: Optional[str] = Field(
        None, description="The head branch name the changes are on."
    )
    head_sha: Optional[str] = Field(
        None, description="The SHA of the head commit that is being checked."
    )
    status: Optional[Status5] = Field(
        None,
        description="The summary status for all check runs that are part of the check suite. Can be `queued`, `requested`, `in_progress`, or `completed`.",
    )
    conclusion: Optional[Conclusion1] = Field(
        None,
        description="The summary conclusion for all check runs that are part of the check suite. Can be one of `success`, `failure`,` neutral`, `cancelled`, `timed_out`, `action_required` or `stale`. This value will be `null` until the check run has completed.",
    )
    url: Optional[AnyUrl] = Field(
        None, description="URL that points to the check suite API resource."
    )
    before: Optional[str] = None
    after: Optional[str] = None
    pull_requests: Optional[List[CheckRunPullRequest]] = Field(
        None,
        description="An array of pull requests that match this check suite. A pull request matches a check suite if they have the same `head_sha` and `head_branch`. When the check suite's `head_branch` is in a forked repository it will be `null` and the `pull_requests` array will be empty.",
    )
    app: Optional[App] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    runs_rerequestable: Optional[bool] = None
    rerequestable: Optional[bool] = None
    latest_check_runs_count: Optional[int] = None
    check_runs_url: Optional[AnyUrl] = None
    head_commit: Optional[CommitSimple] = None


class CheckSuiteRequested(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["requested"]] = None
    check_suite: Optional[CheckSuite5] = Field(
        None,
        description="The [check_suite](https://docs.github.com/en/rest/reference/checks#suites).",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class CheckSuite6(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    node_id: Optional[str] = None
    head_branch: Optional[str] = Field(
        None, description="The head branch name the changes are on."
    )
    head_sha: Optional[str] = Field(
        None, description="The SHA of the head commit that is being checked."
    )
    status: Optional[Status5] = Field(
        None,
        description="The summary status for all check runs that are part of the check suite. Can be `queued`, `requested`, `in_progress`, or `completed`.",
    )
    conclusion: Optional[Conclusion1] = Field(
        None,
        description="The summary conclusion for all check runs that are part of the check suite. Can be one of `success`, `failure`,` neutral`, `cancelled`, `timed_out`, `action_required` or `stale`. This value will be `null` until the check run has completed.",
    )
    url: Optional[AnyUrl] = Field(
        None, description="URL that points to the check suite API resource."
    )
    before: Optional[str] = None
    after: Optional[str] = None
    pull_requests: Optional[List[CheckRunPullRequest]] = Field(
        None,
        description="An array of pull requests that match this check suite. A pull request matches a check suite if they have the same `head_sha` and `head_branch`. When the check suite's `head_branch` is in a forked repository it will be `null` and the `pull_requests` array will be empty.",
    )
    app: Optional[App] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    latest_check_runs_count: Optional[int] = None
    check_runs_url: Optional[AnyUrl] = None
    head_commit: Optional[CommitSimple] = None


class CheckSuiteRerequested(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["rerequested"]] = None
    check_suite: Optional[CheckSuite6] = Field(
        None,
        description="The [check_suite](https://docs.github.com/en/rest/reference/checks#suites).",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class CheckSuiteEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[(CheckSuiteCompleted, CheckSuiteRequested, CheckSuiteRerequested)]
    ] = None


class CodeScanningAlertAppearedInBranch(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["appeared_in_branch"]] = None
    alert: Optional[Alert] = Field(
        None, description="The code scanning alert involved in the event."
    )
    ref: Optional[str] = Field(
        None,
        description="The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.",
    )
    commit_oid: Optional[str] = Field(
        None,
        description="The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.",
    )
    repository: Optional[Repository] = None
    sender: Optional[GithubOrg] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class CodeScanningAlertClosedByUser(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["closed_by_user"]] = None
    alert: Optional[Alert] = Field(
        None, description="The code scanning alert involved in the event."
    )
    ref: Optional[str] = Field(
        None,
        description="The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.",
    )
    commit_oid: Optional[str] = Field(
        None,
        description="The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class CodeScanningAlertCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    alert: Optional[Alert] = Field(
        None, description="The code scanning alert involved in the event."
    )
    ref: Optional[str] = Field(
        None,
        description="The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.",
    )
    commit_oid: Optional[str] = Field(
        None,
        description="The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.",
    )
    repository: Optional[Repository] = None
    sender: Optional[GithubOrg] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class CodeScanningAlertFixed(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["fixed"]] = None
    alert: Optional[Alert] = Field(
        None, description="The code scanning alert involved in the event."
    )
    ref: Optional[str] = Field(
        None,
        description="The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.",
    )
    commit_oid: Optional[str] = Field(
        None,
        description="The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.",
    )
    repository: Optional[Repository] = None
    sender: Optional[GithubOrg] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class CodeScanningAlertReopened(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["reopened"]] = None
    alert: Optional[Alert] = Field(
        None, description="The code scanning alert involved in the event."
    )
    ref: Optional[str] = Field(
        None,
        description="The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.",
    )
    commit_oid: Optional[str] = Field(
        None,
        description="The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.",
    )
    repository: Optional[Repository] = None
    sender: Optional[GithubOrg] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class CodeScanningAlertReopenedByUser(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["reopened_by_user"]] = None
    alert: Optional[Alert] = Field(
        None, description="The code scanning alert involved in the event."
    )
    ref: Optional[str] = Field(
        None,
        description="The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.",
    )
    commit_oid: Optional[str] = Field(
        None,
        description="The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class CodeScanningAlertEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                CodeScanningAlertAppearedInBranch,
                CodeScanningAlertClosedByUser,
                CodeScanningAlertCreated,
                CodeScanningAlertFixed,
                CodeScanningAlertReopened,
                CodeScanningAlertReopenedByUser,
            )
        ]
    ] = None


class CommitCommentCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = Field(
        None, description="The action performed. Can be `created`."
    )
    comment: Optional[Comment] = Field(
        None,
        description="The [commit comment](https://docs.github.com/en/rest/reference/repos#get-a-commit-comment) resource.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class CommitCommentEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[CommitCommentCreated] = None


class CreateEvent(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    ref: Optional[str] = Field(
        None,
        description="The [`git ref`](https://docs.github.com/en/rest/reference/git#get-a-reference) resource.",
    )
    ref_type: Optional[RefType] = Field(
        None,
        description="The type of Git ref object created in the repository. Can be either `branch` or `tag`.",
    )
    master_branch: Optional[str] = Field(
        None,
        description="The name of the repository's default branch (usually `main`).",
    )
    description: Optional[str] = Field(
        None, description="The repository's current description."
    )
    pusher_type: Optional[str] = Field(
        None,
        description="The pusher type for the event. Can be either `user` or a deploy key.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DeleteEvent(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    ref: Optional[str] = Field(
        None,
        description="The [`git ref`](https://docs.github.com/en/rest/reference/git#get-a-reference) resource.",
    )
    ref_type: Optional[RefType] = Field(
        None,
        description="The type of Git ref object deleted in the repository. Can be either `branch` or `tag`.",
    )
    pusher_type: Optional[str] = Field(
        None,
        description="The pusher type for the event. Can be either `user` or a deploy key.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Alert6(DependabotAlert):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["open"]] = None
    fixed_at: None = None
    dismissed_at: None = None
    dismissed_by: None = None
    dismissed_reason: None = None
    dismissed_comment: None = None


class DependabotAlertCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    alert: Optional[Alert6] = None
    repository: Optional[Repository] = None
    sender: Optional[GithubOrg] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Alert7(DependabotAlert):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["dismissed"]] = None
    dismissed_at: Optional[datetime] = None
    dismissed_by: Optional[User] = None
    dismissed_reason: Optional[DismissedReason3] = None


class DependabotAlertDismissed(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["dismissed"]] = None
    alert: Optional[Alert7] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Alert8(DependabotAlert):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["fixed"]] = None
    fixed_at: Optional[datetime] = None


class DependabotAlertFixed(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["fixed"]] = None
    alert: Optional[Alert8] = None
    repository: Optional[Repository] = None
    sender: Optional[GithubOrg] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DependabotAlertReintroduced(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["reintroduced"]] = None
    alert: Optional[DependabotAlert] = None
    repository: Optional[Repository] = None
    sender: Optional[GithubOrg] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DependabotAlertReopened(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["reopened"]] = None
    alert: Optional[DependabotAlert] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DependabotAlertEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                DependabotAlertCreated,
                DependabotAlertDismissed,
                DependabotAlertFixed,
                DependabotAlertReintroduced,
                DependabotAlertReopened,
            )
        ]
    ] = None


class DeployKeyCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    key: Optional[Key] = Field(
        None,
        description="The [`deploy key`](https://docs.github.com/en/rest/reference/deployments#get-a-deploy-key) resource.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DeployKeyDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    key: Optional[Key] = Field(
        None,
        description="The [`deploy key`](https://docs.github.com/en/rest/reference/deployments#get-a-deploy-key) resource.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DeployKeyEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[Union[(DeployKeyCreated, DeployKeyDeleted)]] = None


class DeploymentCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    deployment: Optional[Deployment] = None
    workflow: Optional[Workflow] = None
    workflow_run: Optional[DeploymentWorkflowRun] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DeploymentEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[DeploymentCreated] = None


class DeploymentStatus(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    state: Optional[State4] = Field(
        None,
        description="The new state. Can be `pending`, `success`, `failure`, or `error`.",
    )
    creator: Optional[User] = None
    description: Optional[str] = Field(
        None, description="The optional human-readable description added to the status."
    )
    environment: Optional[str] = None
    environment_url: Optional[Union[(AnyUrl, Literal[""])]] = None
    log_url: Optional[AnyUrl] = None
    target_url: Optional[str] = Field(
        None, description="The optional link added to the status."
    )
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deployment_url: Optional[AnyUrl] = None
    repository_url: Optional[AnyUrl] = None
    performed_via_github_app: Optional[App] = None


class DeploymentStatusCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    deployment_status: Optional[DeploymentStatus] = Field(
        None,
        description="The [deployment status](https://docs.github.com/en/rest/reference/deployments#list-deployment-statuses).",
    )
    deployment: Optional[Deployment] = None
    check_run: Optional[CheckRun4] = None
    workflow_run: Optional[DeploymentWorkflowRun] = None
    workflow: Optional[Workflow] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DeploymentStatusEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[DeploymentStatusCreated] = None


class DiscussionModel(Discussion):
    model_config = ConfigDict(extra="allow")
    category: Optional[Category] = None
    answer_html_url: Optional[AnyUrl] = None
    answer_chosen_at: Optional[datetime] = None
    answer_chosen_by: Optional[User] = None


class DiscussionAnswered(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["answered"]] = None
    discussion: Optional[DiscussionModel] = None
    answer: Optional[Answer] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DiscussionCategoryChanged(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    changes: Optional[Changes1] = None
    action: Optional[Literal["category_changed"]] = None
    discussion: Optional[Discussion] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Discussion1(Discussion):
    model_config = ConfigDict(extra="allow")
    state: Optional[State5] = None
    locked: Optional[Literal[False]] = None
    answer_html_url: None = None
    answer_chosen_at: None = None
    answer_chosen_by: None = None


class DiscussionCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    discussion: Optional[Discussion1] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DiscussionDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    discussion: Optional[Discussion] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DiscussionEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    changes: Optional[Changes2] = None
    action: Optional[Literal["edited"]] = None
    discussion: Optional[Discussion] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DiscussionLabeled(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["labeled"]] = None
    discussion: Optional[Discussion] = None
    label: Optional[Label] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Discussion2(Discussion):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["locked"]] = None
    locked: Optional[Literal[True]] = None


class DiscussionLocked(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["locked"]] = None
    discussion: Optional[Discussion2] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DiscussionPinned(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["pinned"]] = None
    discussion: Optional[Discussion] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Changes3(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    new_discussion: Optional[Discussion] = None
    new_repository: Optional[Repository] = None


class DiscussionTransferred(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    changes: Optional[Changes3] = None
    action: Optional[Literal["transferred"]] = None
    discussion: Optional[Discussion] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Discussion3(Discussion):
    model_config = ConfigDict(extra="allow")
    category: Optional[Category2] = None
    answer_html_url: None = None
    answer_chosen_at: None = None
    answer_chosen_by: None = None


class DiscussionUnanswered(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unanswered"]] = None
    discussion: Optional[Discussion3] = None
    old_answer: Optional[OldAnswer] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DiscussionUnlabeled(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unlabeled"]] = None
    discussion: Optional[Discussion] = None
    label: Optional[Label] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Discussion4(Discussion):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["open"]] = None
    locked: Optional[Literal[False]] = None


class DiscussionUnlocked(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unlocked"]] = None
    discussion: Optional[Discussion4] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DiscussionUnpinned(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unpinned"]] = None
    discussion: Optional[Discussion] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DiscussionEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                DiscussionAnswered,
                DiscussionCategoryChanged,
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
            )
        ]
    ] = None


class DiscussionCommentCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    comment: Optional[Comment1] = None
    discussion: Optional[Discussion] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DiscussionCommentDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    comment: Optional[Comment1] = None
    discussion: Optional[Discussion] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DiscussionCommentEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    changes: Optional[Changes4] = None
    action: Optional[Literal["edited"]] = None
    comment: Optional[Comment1] = None
    discussion: Optional[Discussion] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DiscussionCommentEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                DiscussionCommentCreated,
                DiscussionCommentDeleted,
                DiscussionCommentEdited,
            )
        ]
    ] = None


class Forkee(Repository):
    model_config = ConfigDict(extra="allow")
    fork: Optional[Literal[True]] = None


class ForkEvent(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    forkee: Optional[Forkee] = Field(
        None,
        description="The created [`repository`](https://docs.github.com/en/rest/reference/repos#get-a-repository) resource.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class GollumEvent(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    pages: Optional[List[Page]] = Field(
        None, description="The pages that were updated."
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class InstallationCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    installation: Optional[Installation] = None
    repositories: Optional[List[Repository1]] = Field(
        None,
        description="An array of repository objects that the installation can access.",
    )
    requester: Optional[User] = None
    sender: Optional[User] = None


class InstallationDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    installation: Optional[Installation] = None
    repositories: Optional[List[Repository1]] = Field(
        None,
        description="An array of repository objects that the installation can access.",
    )
    requester: None = None
    sender: Optional[User] = None


class InstallationNewPermissionsAccepted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["new_permissions_accepted"]] = None
    installation: Optional[Installation] = None
    repositories: Optional[List[Repository1]] = Field(
        None,
        description="An array of repository objects that the installation can access.",
    )
    requester: None = None
    sender: Optional[User] = None


class Installation1(Installation):
    model_config = ConfigDict(extra="allow")
    suspended_by: Optional[User] = None
    suspended_at: Optional[datetime] = None


class InstallationSuspend(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["suspend"]] = None
    installation: Optional[Installation1] = None
    repositories: Optional[List[Repository1]] = Field(
        None,
        description="An array of repository objects that the installation can access.",
    )
    requester: None = None
    sender: Optional[User] = None


class Installation2(Installation):
    model_config = ConfigDict(extra="allow")
    suspended_by: None = None
    suspended_at: None = None


class InstallationUnsuspend(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unsuspend"]] = None
    installation: Optional[Installation2] = None
    repositories: Optional[List[Repository1]] = Field(
        None,
        description="An array of repository objects that the installation can access.",
    )
    requester: None = None
    sender: Optional[User] = None


class InstallationEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                InstallationCreated,
                InstallationDeleted,
                InstallationNewPermissionsAccepted,
                InstallationSuspend,
                InstallationUnsuspend,
            )
        ]
    ] = None


class InstallationRepositoriesAdded(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["added"]] = None
    installation: Optional[Installation] = None
    repository_selection: Optional[RepositorySelection] = Field(
        None,
        description="Describe whether all repositories have been selected or there's a selection involved",
    )
    repositories_added: Optional[List[RepositoriesAddedItem]] = Field(
        None,
        description="An array of repository objects, which were added to the installation.",
    )
    repositories_removed: Optional[List[RepositoriesRemovedItem]] = Field(
        None,
        description="An array of repository objects, which were removed from the installation.",
        max_length=0,
    )
    requester: Optional[User] = None
    sender: Optional[User] = None


class InstallationRepositoriesRemoved(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["removed"]] = None
    installation: Optional[Installation] = None
    repository_selection: Optional[RepositorySelection] = Field(
        None,
        description="Describe whether all repositories have been selected or there's a selection involved",
    )
    repositories_added: Optional[List[RepositoriesAddedItem]] = Field(
        None,
        description="An array of repository objects, which were added to the installation.",
        max_length=0,
    )
    repositories_removed: Optional[List[RepositoriesRemovedItem]] = Field(
        None,
        description="An array of repository objects, which were removed from the installation.",
    )
    requester: Optional[User] = None
    sender: Optional[User] = None


class InstallationRepositoriesEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[(InstallationRepositoriesAdded, InstallationRepositoriesRemoved)]
    ] = None


class InstallationTargetRenamed(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    changes: Optional[Changes5] = None
    action: Optional[Literal["renamed"]] = None
    account: Optional[Account] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    target_type: Optional[str] = None


class InstallationTargetEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[InstallationTargetRenamed] = None


class LabelCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    label: Optional[Label] = Field(None, description="The label that was added.")
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class LabelDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    label: Optional[Label] = Field(None, description="The label that was removed.")
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class LabelEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    label: Optional[Label] = Field(None, description="The label that was edited.")
    changes: Optional[Changes10] = Field(
        None, description="The changes to the label if the action was `edited`."
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class LabelEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[Union[(LabelCreated, LabelDeleted, LabelEdited)]] = None


class MemberAdded(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["added"]] = None
    changes: Optional[Changes11] = None
    member: Optional[User] = Field(None, description="The user that was added.")
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class MemberEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    member: Optional[User] = Field(
        None, description="The user who's permissions are changed."
    )
    changes: Optional[Changes12] = Field(
        None, description="The changes to the collaborator permissions"
    )
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class MemberRemoved(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["removed"]] = None
    member: Optional[User] = Field(None, description="The user that was removed.")
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class MemberEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[Union[(MemberAdded, MemberEdited, MemberRemoved)]] = None


class MergeGroupChecksRequested(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["checks_requested"]] = None
    merge_group: Optional[MergeGroup] = Field(None, description="The merge group.")
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class MergeGroupEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[MergeGroupChecksRequested] = None


class MetaDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    hook_id: Optional[int] = Field(None, description="The id of the modified webhook.")
    hook: Optional[Hook] = Field(
        None,
        description="The modified webhook. This will contain different keys based on the type of webhook it is: repository, organization, business, app, or GitHub Marketplace.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None


class MetaEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[MetaDeleted] = None


class Milestone1(Milestone):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["closed"]] = None
    closed_at: Optional[str] = None


class MilestoneClosed(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["closed"]] = None
    milestone: Optional[Milestone1] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Milestone2(Milestone):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["open"]] = None
    closed_at: None = None


class MilestoneCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    milestone: Optional[Milestone2] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class MilestoneDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    milestone: Optional[Milestone] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class MilestoneEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    changes: Optional[Changes13] = Field(
        None, description="The changes to the milestone if the action was `edited`."
    )
    milestone: Optional[Milestone] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class MilestoneOpened(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["opened"]] = None
    milestone: Optional[Milestone2] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class MilestoneEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                MilestoneClosed,
                MilestoneCreated,
                MilestoneDeleted,
                MilestoneEdited,
                MilestoneOpened,
            )
        ]
    ] = None


class OrganizationDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    membership: Optional[Membership] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class OrganizationMemberAdded(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["member_added"]] = None
    membership: Optional[Membership] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class OrganizationMemberRemoved(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["member_removed"]] = None
    membership: Optional[Membership] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class OrganizationEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                OrganizationDeleted,
                OrganizationMemberAdded,
                OrganizationMemberInvited,
                OrganizationMemberRemoved,
                OrganizationRenamed,
            )
        ]
    ] = None


class Repository6(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    repository: Optional[Repository] = None


class BodyItem(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    repository: Optional[Repository6] = None
    info: Optional[Info] = None
    attributes: Optional[Dict[(str, Any)]] = None
    field_formatted: Optional[bool] = Field(None, alias="_formatted")


class PackageVersionItem(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(
        None, description="Unique identifier of the package version."
    )
    version: Optional[str] = None
    summary: Optional[str] = None
    name: Optional[str] = Field(None, description="The name of the package version.")
    description: Optional[str] = None
    body: Optional[Union[(str, BodyItem)]] = None
    body_html: Optional[str] = None
    release: Optional[Release] = None
    manifest: Optional[str] = None
    html_url: Optional[AnyUrl] = None
    tag_name: Optional[str] = None
    target_commitish: Optional[str] = None
    target_oid: Optional[str] = None
    draft: Optional[bool] = None
    prerelease: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    metadata: Optional[List] = Field(None, description="Package Version Metadata")
    container_metadata: Optional[ContainerMetadatum] = None
    docker_metadata: Optional[List] = None
    npm_metadata: Optional[PackageNpmMetadata] = None
    nuget_metadata: Optional[List[PackageNugetMetadata]] = None
    rubygems_metadata: Optional[List] = None
    package_files: Optional[List[PackageFile]] = None
    package_url: Optional[str] = None
    author: Optional[User] = None
    source_url: Optional[str] = None
    installation_command: Optional[str] = None


class Package(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="Unique identifier of the package.")
    name: Optional[str] = Field(None, description="The name of the package.")
    namespace: Optional[str] = None
    description: Optional[str] = None
    ecosystem: Optional[str] = None
    package_type: Optional[PackageType] = Field(
        None,
        description="The type of supported package. Packages in GitHub's Gradle registry have the type `maven`. Docker images pushed to GitHub's Container registry (`ghcr.io`) have the type `container`. You can use the type `docker` to find images that were pushed to GitHub's Docker registry (`docker.pkg.github.com`), even if these have now been migrated to the Container registry.",
    )
    html_url: Optional[AnyUrl] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    owner: Optional[User] = None
    package_version: Optional[PackageVersionItem] = Field(
        None, description="A version of a software package"
    )
    registry: Optional[Registry] = None


class PackagePublished(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["published"]] = None
    package: Optional[Package] = Field(
        None, description="Information about the package."
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class BodyItem1(BodyItem):
    pass


class PackageVersionItem1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(
        None, description="Unique identifier of the package version."
    )
    version: Optional[str] = None
    summary: Optional[str] = None
    name: Optional[str] = Field(None, description="The name of the package version.")
    description: Optional[str] = None
    body: Optional[Union[(str, BodyItem1)]] = None
    body_html: Optional[str] = None
    release: Optional[Release] = None
    manifest: Optional[str] = None
    html_url: Optional[AnyUrl] = None
    tag_name: Optional[str] = None
    target_commitish: Optional[str] = None
    target_oid: Optional[str] = None
    draft: Optional[bool] = None
    prerelease: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    metadata: Optional[List] = Field(None, description="Package Version Metadata")
    container_metadata: Optional[ContainerMetadatum1] = None
    docker_metadata: Optional[List] = None
    npm_metadata: Optional[PackageNpmMetadata] = None
    nuget_metadata: Optional[List[PackageNugetMetadata]] = None
    rubygems_metadata: Optional[List] = None
    package_files: Optional[List[PackageFile]] = None
    package_url: Optional[str] = None
    author: Optional[User] = None
    source_url: Optional[str] = None
    installation_command: Optional[str] = None


class Package1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="Unique identifier of the package.")
    name: Optional[str] = Field(None, description="The name of the package.")
    namespace: Optional[str] = None
    description: Optional[str] = None
    ecosystem: Optional[str] = None
    package_type: Optional[PackageType] = None
    html_url: Optional[AnyUrl] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    owner: Optional[User] = None
    package_version: Optional[PackageVersionItem1] = Field(
        None, description="A version of a software package"
    )
    registry: Optional[Registry] = None


class PackageUpdated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["updated"]] = None
    package: Optional[Package1] = Field(
        None, description="Information about the package."
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class PackageEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[Union[(PackagePublished, PackageUpdated)]] = None


class PageBuildEvent(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = None
    build: Optional[Build] = Field(
        None,
        description="The [List GitHub Pages builds](https://docs.github.com/en/rest/reference/repos#list-github-pages-builds) itself.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class PingEvent(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    zen: Optional[str] = None
    hook_id: Optional[int] = Field(
        None, description="The ID of the webhook that triggered the ping."
    )
    hook: Optional[Hook1] = Field(
        None,
        description="The [webhook configuration](https://docs.github.com/en/rest/reference/repos#get-a-repository-webhook).",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None


class ProjectClosed(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["closed"]] = None
    project: Optional[Project] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class ProjectCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    project: Optional[Project] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class ProjectDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    project: Optional[Project] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class ProjectEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    changes: Optional[Changes15] = Field(
        None, description="The changes to the project if the action was `edited`."
    )
    project: Optional[Project] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class ProjectReopened(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["reopened"]] = None
    project: Optional[Project] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class ProjectEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                ProjectClosed,
                ProjectCreated,
                ProjectDeleted,
                ProjectEdited,
                ProjectReopened,
            )
        ]
    ] = None


class ProjectCardConverted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["converted"]] = None
    changes: Optional[Changes16] = None
    project_card: Optional[ProjectCard] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class ProjectCardCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    project_card: Optional[ProjectCard] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class ProjectCardDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    project_card: Optional[ProjectCard] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class ProjectCardEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    changes: Optional[Changes17] = None
    project_card: Optional[ProjectCard] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class ProjectCard1(ProjectCard):
    model_config = ConfigDict(extra="allow")
    after_id: Optional[float] = None


class ProjectCardMoved(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["moved"]] = None
    changes: Optional[Changes18] = None
    project_card: Optional[ProjectCard1] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class ProjectCardEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                ProjectCardConverted,
                ProjectCardCreated,
                ProjectCardDeleted,
                ProjectCardEdited,
                ProjectCardMoved,
            )
        ]
    ] = None


class ProjectColumnCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    project_column: Optional[ProjectColumn] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class ProjectColumnDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    project_column: Optional[ProjectColumn] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class ProjectColumnEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    changes: Optional[Changes19] = None
    project_column: Optional[ProjectColumn] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class ProjectColumnMoved(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["moved"]] = None
    project_column: Optional[ProjectColumn] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class ProjectColumnEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                ProjectColumnCreated,
                ProjectColumnDeleted,
                ProjectColumnEdited,
                ProjectColumnMoved,
            )
        ]
    ] = None


class ProjectsV2ItemModel(ProjectsV2Item):
    model_config = ConfigDict(extra="allow")
    archived_at: Optional[datetime] = None


class ProjectsV2ItemArchived(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    changes: Optional[Changes20] = None
    action: Optional[Literal["archived"]] = None
    projects_v2_item: Optional[ProjectsV2ItemModel] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class ProjectsV2Item1(ProjectsV2Item):
    model_config = ConfigDict(extra="allow")
    content_type: Optional[Literal["Issue"]] = None


class ProjectsV2ItemConverted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    changes: Optional[Changes21] = None
    action: Optional[Literal["converted"]] = None
    projects_v2_item: Optional[ProjectsV2Item1] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class ProjectsV2Item2(ProjectsV2Item):
    model_config = ConfigDict(extra="allow")
    archived_at: None = None


class ProjectsV2ItemCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    projects_v2_item: Optional[ProjectsV2Item2] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class ProjectsV2ItemDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    projects_v2_item: Optional[ProjectsV2Item] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class ProjectsV2ItemEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    changes: Optional[Changes22] = None
    action: Optional[Literal["edited"]] = None
    projects_v2_item: Optional[ProjectsV2Item] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class ProjectsV2ItemReordered(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    changes: Optional[Changes23] = None
    action: Optional[Literal["reordered"]] = None
    projects_v2_item: Optional[ProjectsV2Item] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class ProjectsV2ItemRestored(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    changes: Optional[Changes24] = None
    action: Optional[Literal["restored"]] = None
    projects_v2_item: Optional[ProjectsV2Item2] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class ProjectsV2ItemEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                ProjectsV2ItemArchived,
                ProjectsV2ItemConverted,
                ProjectsV2ItemCreated,
                ProjectsV2ItemDeleted,
                ProjectsV2ItemEdited,
                ProjectsV2ItemReordered,
                ProjectsV2ItemRestored,
            )
        ]
    ] = None


class Repository8(Repository):
    model_config = ConfigDict(extra="allow")
    private: Optional[Literal[False]] = None


class PublicEvent(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    repository: Optional[Repository8] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Review(PullRequestReview):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["dismissed"]] = None


class PullRequestReviewDismissed(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["dismissed"]] = None
    review: Optional[Review] = None
    pull_request: Optional[SimplePullRequest] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestReviewEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    changes: Optional[Changes26] = None
    review: Optional[PullRequestReview] = None
    pull_request: Optional[SimplePullRequest] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestReviewSubmitted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["submitted"]] = None
    review: Optional[PullRequestReview] = None
    pull_request: Optional[SimplePullRequest] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestReviewEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                PullRequestReviewDismissed,
                PullRequestReviewEdited,
                PullRequestReviewSubmitted,
            )
        ]
    ] = None


class PullRequest8(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    html_url: Optional[AnyUrl] = None
    diff_url: Optional[AnyUrl] = None
    patch_url: Optional[AnyUrl] = None
    issue_url: Optional[AnyUrl] = None
    number: Optional[int] = None
    state: Optional[State6] = None
    locked: Optional[bool] = None
    title: Optional[str] = None
    user: Optional[User] = None
    body: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    merged_at: Optional[datetime] = None
    merge_commit_sha: Optional[str] = None
    assignee: Optional[User] = None
    assignees: Optional[List[User]] = None
    requested_reviewers: Optional[List[Union[(User, Team)]]] = None
    requested_teams: Optional[List[Team]] = None
    labels: Optional[List[Label]] = None
    milestone: Optional[Milestone] = None
    draft: Optional[bool] = None
    commits_url: Optional[AnyUrl] = None
    review_comments_url: Optional[AnyUrl] = None
    review_comment_url: Optional[str] = None
    comments_url: Optional[AnyUrl] = None
    statuses_url: Optional[AnyUrl] = None
    head: Optional[Head5] = None
    base: Optional[Base6] = None
    links: Optional[Links5] = Field(None, alias="_links")
    auto_merge: Optional[AutoMerge] = None
    author_association: Optional[AuthorAssociation] = None
    active_lock_reason: Optional[ActiveLockReason] = None


class PullRequestReviewCommentCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    comment: Optional[PullRequestReviewComment] = None
    pull_request: Optional[PullRequest8] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequest9(PullRequest8):
    pass


class PullRequestReviewCommentDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    comment: Optional[PullRequestReviewComment] = None
    pull_request: Optional[PullRequest9] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequest10(PullRequest8):
    pass


class PullRequestReviewCommentEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    changes: Optional[Changes27] = Field(
        None, description="The changes to the comment."
    )
    comment: Optional[PullRequestReviewComment] = None
    pull_request: Optional[PullRequest10] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestReviewCommentEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                PullRequestReviewCommentCreated,
                PullRequestReviewCommentDeleted,
                PullRequestReviewCommentEdited,
            )
        ]
    ] = None


class Thread(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    node_id: Optional[str] = None
    comments: Optional[List[PullRequestReviewComment]] = None


class PullRequestReviewThreadResolved(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["resolved"]] = None
    thread: Optional[Thread] = None
    pull_request: Optional[SimplePullRequest] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestReviewThreadUnresolved(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unresolved"]] = None
    thread: Optional[Thread] = None
    pull_request: Optional[SimplePullRequest] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestReviewThreadEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[(PullRequestReviewThreadResolved, PullRequestReviewThreadUnresolved)]
    ] = None


class PushEvent(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    ref: Optional[str] = Field(
        None,
        description="The full git ref that was pushed. Example: `refs/heads/main` or `refs/tags/v3.14.1`.",
    )
    before: Optional[str] = Field(
        None, description="The SHA of the most recent commit on `ref` before the push."
    )
    after: Optional[str] = Field(
        None, description="The SHA of the most recent commit on `ref` after the push."
    )
    created: Optional[bool] = Field(
        None, description="Whether this push created the `ref`."
    )
    deleted: Optional[bool] = Field(
        None, description="Whether this push deleted the `ref`."
    )
    forced: Optional[bool] = Field(
        None, description="Whether this push was a force push of the `ref`."
    )
    base_ref: Optional[str] = None
    compare: Optional[str] = Field(
        None,
        description="URL that shows the changes in this `ref` update, from the `before` commit to the `after` commit. For a newly created `ref` that is directly based on the default branch, this is the comparison between the head of the default branch and the `after` commit. Otherwise, this shows all commits until the `after` commit.",
    )
    commits: Optional[List[Commit]] = Field(
        None,
        description="An array of commit objects describing the pushed commits. (Pushed commits are all commits that are included in the `compare` between the `before` commit and the `after` commit.) The array includes a maximum of 20 commits. If necessary, you can use the [Commits API](https://docs.github.com/en/rest/reference/repos#commits) to fetch additional commits. This limit is applied to timeline events only and isn't applied to webhook deliveries.",
    )
    head_commit: Optional[Commit] = Field(
        None,
        description="For pushes where `after` is or points to a commit object, an expanded representation of that commit. For pushes where `after` refers to an annotated tag object, an expanded representation of the commit pointed to by the annotated tag.",
    )
    repository: Optional[Repository] = None
    pusher: Optional[CommitterModel] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Repository9(Repository6):
    pass


class BodyItem2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    repository: Optional[Repository9] = None
    info: Optional[Info2] = None
    attributes: Optional[Dict[(str, Any)]] = None
    field_formatted: Optional[bool] = Field(None, alias="_formatted")


class PackageVersionItem2(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(
        None, description="Unique identifier of the package version."
    )
    version: Optional[str] = None
    summary: Optional[str] = None
    name: Optional[str] = Field(None, description="The name of the package version.")
    description: Optional[str] = None
    body: Optional[Union[(str, BodyItem2)]] = None
    body_html: Optional[str] = None
    release: Optional[Release] = None
    manifest: Optional[str] = None
    html_url: Optional[AnyUrl] = None
    tag_name: Optional[str] = None
    target_commitish: Optional[str] = None
    target_oid: Optional[str] = None
    draft: Optional[bool] = None
    prerelease: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    metadata: Optional[List] = Field(None, description="Package Version Metadata")
    docker_metadata: Optional[List] = None
    container_metadata: Optional[ContainerMetadata] = None
    npm_metadata: Optional[PackageNpmMetadata] = None
    nuget_metadata: Optional[List[PackageNugetMetadata]] = None
    rubygems_metadata: Optional[List] = None
    package_files: Optional[List[PackageFile]] = None
    package_url: Optional[str] = None
    author: Optional[Author1] = None
    source_url: Optional[str] = None
    installation_command: Optional[str] = None


class RegistryPackage(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="Unique identifier of the package.")
    name: Optional[str] = Field(None, description="The name of the package.")
    namespace: Optional[str] = None
    description: Optional[str] = None
    ecosystem: Optional[str] = None
    package_type: Optional[PackageType] = Field(
        None,
        description="The type of supported package. Packages in GitHub's Gradle registry have the type `maven`. Docker images pushed to GitHub's Container registry (`ghcr.io`) have the type `container`. You can use the type `docker` to find images that were pushed to GitHub's Docker registry (`docker.pkg.github.com`), even if these have now been migrated to the Container registry.",
    )
    html_url: Optional[AnyUrl] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    owner: Optional[User] = None
    package_version: Optional[PackageVersionItem2] = Field(
        None, description="A version of a software package"
    )
    registry: Optional[Registry] = None


class RegistryPackagePublished(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["published"]] = None
    registry_package: Optional[RegistryPackage] = Field(
        None, description="Information about the package."
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class BodyItem3(BodyItem2):
    pass


class PackageVersionItem3(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(
        None, description="Unique identifier of the package version."
    )
    version: Optional[str] = None
    summary: Optional[str] = None
    name: Optional[str] = Field(None, description="The name of the package version.")
    description: Optional[str] = None
    body: Optional[Union[(str, BodyItem3)]] = None
    body_html: Optional[str] = None
    release: Optional[Release] = None
    manifest: Optional[str] = None
    html_url: Optional[AnyUrl] = None
    tag_name: Optional[str] = None
    target_commitish: Optional[str] = None
    target_oid: Optional[str] = None
    draft: Optional[bool] = None
    prerelease: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    metadata: Optional[List] = Field(None, description="Package Version Metadata")
    docker_metadata: Optional[List] = None
    container_metadata: Optional[ContainerMetadata1] = None
    npm_metadata: Optional[PackageNpmMetadata] = None
    nuget_metadata: Optional[List[PackageNugetMetadata]] = None
    rubygems_metadata: Optional[List] = None
    package_files: Optional[List[PackageFile]] = None
    package_url: Optional[str] = None
    author: Optional[Author1] = None
    source_url: Optional[str] = None
    installation_command: Optional[str] = None


class RegistryPackage1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="Unique identifier of the package.")
    name: Optional[str] = Field(None, description="The name of the package.")
    namespace: Optional[str] = None
    description: Optional[str] = None
    ecosystem: Optional[str] = None
    package_type: Optional[PackageType] = Field(
        None,
        description="The type of supported package. Packages in GitHub's Gradle registry have the type `maven`. Docker images pushed to GitHub's Container registry (`ghcr.io`) have the type `container`. You can use the type `docker` to find images that were pushed to GitHub's Docker registry (`docker.pkg.github.com`), even if these have now been migrated to the Container registry.",
    )
    html_url: Optional[AnyUrl] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    owner: Optional[User] = None
    package_version: Optional[PackageVersionItem3] = Field(
        None, description="A version of a software package"
    )
    registry: Optional[Registry] = None


class RegistryPackageUpdated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["updated"]] = None
    registry_package: Optional[RegistryPackage1] = Field(
        None, description="Information about the package."
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class RegistryPackageEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[Union[(RegistryPackagePublished, RegistryPackageUpdated)]] = None


class ReleaseCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    release: Optional[ReleaseModel] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class ReleaseDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    release: Optional[ReleaseModel] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class ReleaseEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    changes: Optional[Changes28] = None
    release: Optional[ReleaseModel] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Release4(ReleaseModel):
    model_config = ConfigDict(extra="allow")
    prerelease: Optional[Literal[True]] = Field(
        None,
        description="Whether the release is identified as a prerelease or a full release.",
    )


class ReleasePrereleased(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["prereleased"]] = None
    release: Optional[Release4] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Release5(ReleaseModel):
    model_config = ConfigDict(extra="allow")
    published_at: Optional[datetime] = None


class ReleasePublished(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["published"]] = None
    release: Optional[Release5] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class ReleaseReleased(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["released"]] = None
    release: Optional[ReleaseModel] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Release6(ReleaseModel):
    model_config = ConfigDict(extra="allow")
    published_at: None = None


class ReleaseUnpublished(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unpublished"]] = None
    release: Optional[Release6] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class ReleaseEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                ReleaseCreated,
                ReleaseDeleted,
                ReleaseEdited,
                ReleasePrereleased,
                ReleasePublished,
                ReleaseReleased,
                ReleaseUnpublished,
            )
        ]
    ] = None


class Repository11(Repository):
    model_config = ConfigDict(extra="allow")
    archived: Optional[Literal[True]] = Field(
        False, description="Whether the repository is archived."
    )


class RepositoryArchived(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["archived"]] = None
    repository: Optional[Repository11] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class RepositoryCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class RepositoryDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class RepositoryEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    changes: Optional[Changes29] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Repository12(Repository):
    model_config = ConfigDict(extra="allow")
    private: Optional[Literal[True]] = Field(
        None, description="Whether the repository is private or public."
    )


class RepositoryPrivatized(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["privatized"]] = None
    repository: Optional[Repository12] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Repository13(Repository):
    model_config = ConfigDict(extra="allow")
    private: Optional[Literal[False]] = Field(
        None, description="Whether the repository is private or public."
    )


class RepositoryPublicized(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["publicized"]] = None
    repository: Optional[Repository13] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class RepositoryRenamed(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["renamed"]] = None
    changes: Optional[Changes30] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class RepositoryTransferred(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["transferred"]] = None
    changes: Optional[Changes31] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Repository15(Repository):
    model_config = ConfigDict(extra="allow")
    archived: Optional[Literal[False]] = Field(
        False, description="Whether the repository is archived."
    )


class RepositoryUnarchived(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unarchived"]] = None
    repository: Optional[Repository15] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class RepositoryEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
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
        ]
    ] = None


class RepositoryDispatchEvent(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[str] = None
    branch: Optional[str] = None
    client_payload: Optional[Dict[(str, Any)]] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class RepositoryImportEvent(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    status: Optional[Status9] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Alert9(RepositoryVulnerabilityAlertAlert):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["open"]] = None


class RepositoryVulnerabilityAlertCreate(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["create"]] = None
    alert: Optional[Alert9] = None
    repository: Optional[Repository] = None
    sender: Optional[GithubOrg] = None
    organization: Optional[Organization] = None


class Alert10(RepositoryVulnerabilityAlertAlert):
    model_config = ConfigDict(extra="allow")
    dismisser: Optional[User] = None
    dismiss_reason: Optional[str] = None
    dismissed_at: Optional[str] = None
    state: Optional[Literal["dismissed"]] = None


class RepositoryVulnerabilityAlertDismiss(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["dismiss"]] = None
    alert: Optional[Alert10] = None
    repository: Optional[Repository] = None
    sender: Optional[GithubOrg] = None
    organization: Optional[Organization] = None


class Alert11(Alert9):
    pass


class RepositoryVulnerabilityAlertReopen(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["reopen"]] = None
    alert: Optional[Alert11] = None
    repository: Optional[Repository] = None
    sender: Optional[GithubOrg] = None
    organization: Optional[Organization] = None


class Alert12(RepositoryVulnerabilityAlertAlert):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["fixed"]] = None
    fixed_at: Optional[datetime] = None
    fix_reason: Optional[str] = None
    fixed_in: Optional[str] = None


class RepositoryVulnerabilityAlertResolve(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["resolve"]] = None
    alert: Optional[Alert12] = None
    repository: Optional[Repository] = None
    sender: Optional[GithubOrg] = None
    organization: Optional[Organization] = None


class RepositoryVulnerabilityAlertEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                RepositoryVulnerabilityAlertCreate,
                RepositoryVulnerabilityAlertDismiss,
                RepositoryVulnerabilityAlertReopen,
                RepositoryVulnerabilityAlertResolve,
            )
        ]
    ] = None


class Alert13(SecretScanningAlert):
    model_config = ConfigDict(extra="allow")
    resolution: None = None
    resolved_by: None = None
    resolved_at: None = None


class SecretScanningAlertCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    alert: Optional[Alert13] = None
    repository: Optional[Repository] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class SecretScanningAlertReopened(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["reopened"]] = None
    alert: Optional[Alert14] = Field(
        None, description="The secret scanning alert involved in the event."
    )
    repository: Optional[Repository] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None
    sender: Optional[User] = None


class Alert15(SecretScanningAlert):
    model_config = ConfigDict(extra="allow")
    resolution: Optional[Resolution] = None
    resolved_by: Optional[User] = None
    resolved_at: Optional[datetime] = None


class SecretScanningAlertResolved(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["resolved"]] = None
    alert: Optional[Alert15] = None
    repository: Optional[Repository] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None
    sender: Optional[User] = None


class Alert16(SecretScanningAlert):
    model_config = ConfigDict(extra="allow")
    resolution: Optional[Literal["revoked"]] = None
    resolved_by: Optional[User] = None
    resolved_at: Optional[datetime] = None


class SecretScanningAlertRevoked(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["revoked"]] = None
    alert: Optional[Alert16] = None
    repository: Optional[Repository] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None
    sender: Optional[User] = None


class SecretScanningAlertEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                SecretScanningAlertCreated,
                SecretScanningAlertReopened,
                SecretScanningAlertResolved,
                SecretScanningAlertRevoked,
            )
        ]
    ] = None


class SecretScanningAlertLocationCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    alert: Optional[SecretScanningAlert] = None
    location: Optional[SecretScanningLocation] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class SecretScanningAlertLocationEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[SecretScanningAlertLocationCreated] = None


class StarCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    starred_at: Optional[datetime] = Field(
        None,
        description="The time the star was created. This is a timestamp in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. Will be `null` for the `deleted` action.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class StarDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    starred_at: None = Field(
        None,
        description="The time the star was created. This is a timestamp in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. Will be `null` for the `deleted` action.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class StarEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[Union[(StarCreated, StarDeleted)]] = None


class StatusEvent(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    id: Optional[int] = Field(None, description="The unique identifier of the status.")
    sha: Optional[str] = Field(None, description="The Commit SHA.")
    name: Optional[str] = None
    avatar_url: Optional[AnyUrl] = None
    target_url: Optional[str] = Field(
        None, description="The optional link added to the status."
    )
    context: Optional[str] = None
    description: Optional[str] = Field(
        None, description="The optional human-readable description added to the status."
    )
    state: Optional[State12] = Field(
        None,
        description="The new state. Can be `pending`, `success`, `failure`, or `error`.",
    )
    commit: Optional[Commit1] = None
    branches: Optional[List[Branch]] = Field(
        None,
        description="An array of branch objects containing the status' SHA. Each branch contains the given SHA, but the SHA may or may not be the head of the branch. The array includes a maximum of 10 branches.",
    )
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class TeamAddedToRepository(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["added_to_repository"]] = None
    team: Optional[Team] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class TeamCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    team: Optional[Team] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class TeamDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    team: Optional[Team] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class TeamEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    changes: Optional[Changes35] = Field(
        None, description="The changes to the team if the action was `edited`."
    )
    team: Optional[Team] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class TeamRemovedFromRepository(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["removed_from_repository"]] = None
    team: Optional[Team] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None


class TeamEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                TeamAddedToRepository,
                TeamCreated,
                TeamDeleted,
                TeamEdited,
                TeamRemovedFromRepository,
            )
        ]
    ] = None


class TeamAddEvent(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    team: Optional[Team] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class WatchStarted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["started"]] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class WatchEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[WatchStarted] = None


class WorkflowDispatchEvent(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    inputs: Optional[Dict[(str, Any)]] = Field(
        None,
        description="Inputs to the workflow. Each key represents the name of the input while it's value represents the value of that input.",
    )
    ref: Optional[str] = Field(
        None, description="The branch ref from which the workflow was run."
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    workflow: Optional[str] = Field(
        None,
        description="Relative path to the workflow file which contains the workflow.",
    )


class WorkflowJobModel(WorkflowJob):
    model_config = ConfigDict(extra="allow")
    conclusion: Optional[Conclusion12] = None


class WorkflowJobCompleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["completed"]] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    deployment: Optional[Deployment] = None
    workflow_job: Optional[WorkflowJobModel] = None


class WorkflowJob1(WorkflowJob):
    model_config = ConfigDict(extra="allow")
    status: Optional[Status10] = None


class WorkflowJobInProgress(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["in_progress"]] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    deployment: Optional[Deployment] = None
    workflow_job: Optional[WorkflowJob1] = None


class WorkflowJob2(WorkflowJob):
    model_config = ConfigDict(extra="allow")
    status: Optional[Status11] = None


class WorkflowJobQueued(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["queued"]] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    deployment: Optional[Deployment] = None
    workflow_job: Optional[WorkflowJob2] = None


class WorkflowJob3(WorkflowJob):
    model_config = ConfigDict(extra="allow")
    status: Optional[Literal["waiting"]] = None


class WorkflowJobWaiting(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["waiting"]] = None
    organization: Optional[Organization] = None
    installation: Optional[InstallationLite] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    deployment: Optional[Deployment] = None
    workflow_job: Optional[WorkflowJob3] = None


class WorkflowJobEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                WorkflowJobCompleted,
                WorkflowJobInProgress,
                WorkflowJobQueued,
                WorkflowJobWaiting,
            )
        ]
    ] = None


class WorkflowRunModel(WorkflowRun):
    model_config = ConfigDict(extra="allow")
    conclusion: Optional[Conclusion13] = None


class WorkflowRunCompleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["completed"]] = None
    organization: Optional[Organization] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    workflow: Optional[Workflow] = None
    workflow_run: Optional[WorkflowRunModel] = None
    installation: Optional[InstallationLite] = None


class WorkflowRunInProgress(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["in_progress"]] = None
    organization: Optional[Organization] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    workflow: Optional[Workflow] = None
    workflow_run: Optional[WorkflowRun] = None
    installation: Optional[InstallationLite] = None


class WorkflowRunRequested(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["requested"]] = None
    organization: Optional[Organization] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    workflow: Optional[Workflow] = None
    workflow_run: Optional[WorkflowRun] = None
    installation: Optional[InstallationLite] = None


class WorkflowRunEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[(WorkflowRunCompleted, WorkflowRunInProgress, WorkflowRunRequested)]
    ] = None


class Issue(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = Field(None, description="URL for the issue")
    repository_url: Optional[AnyUrl] = None
    labels_url: Optional[str] = None
    comments_url: Optional[AnyUrl] = None
    events_url: Optional[AnyUrl] = None
    html_url: Optional[AnyUrl] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    number: Optional[int] = Field(
        None, description="Number uniquely identifying the issue within its repository"
    )
    title: Optional[str] = Field(None, description="Title of the issue")
    user: Optional[User] = None
    labels: Optional[List[Label]] = None
    state: Optional[State6] = Field(
        None, description="State of the issue; either 'open' or 'closed'"
    )
    locked: Optional[bool] = None
    assignee: Optional[User] = None
    assignees: Optional[List[User]] = None
    milestone: Optional[Milestone] = None
    comments: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    author_association: Optional[AuthorAssociation] = None
    active_lock_reason: Optional[ActiveLockReason] = None
    draft: Optional[bool] = None
    performed_via_github_app: Optional[App] = None
    pull_request: Optional[PullRequest11] = None
    body: Optional[str] = Field(None, description="Contents of the issue")
    reactions: Optional[Reactions] = None
    timeline_url: Optional[AnyUrl] = None
    state_reason: Optional[str] = Field(
        None, description="The reason for the current state"
    )


class Head4(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    label: Optional[str] = None
    ref: Optional[str] = None
    sha: Optional[str] = None
    user: Optional[User] = None
    repo: Optional[Repository] = None


class PullRequest(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    url: Optional[AnyUrl] = None
    id: Optional[int] = None
    node_id: Optional[str] = None
    html_url: Optional[AnyUrl] = None
    diff_url: Optional[AnyUrl] = None
    patch_url: Optional[AnyUrl] = None
    issue_url: Optional[AnyUrl] = None
    number: Optional[int] = Field(
        None,
        description="Number uniquely identifying the pull request within its repository.",
    )
    state: Optional[State6] = Field(
        None, description="State of this Pull Request. Either `open` or `closed`."
    )
    locked: Optional[bool] = None
    title: Optional[str] = Field(None, description="The title of the pull request.")
    user: Optional[User] = None
    body: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    merged_at: Optional[datetime] = None
    merge_commit_sha: Optional[str] = None
    assignee: Optional[User] = None
    assignees: Optional[List[User]] = None
    requested_reviewers: Optional[List[Union[(User, Team)]]] = None
    requested_teams: Optional[List[Team]] = None
    labels: Optional[List[Label]] = None
    milestone: Optional[Milestone] = None
    commits_url: Optional[AnyUrl] = None
    review_comments_url: Optional[AnyUrl] = None
    review_comment_url: Optional[str] = None
    comments_url: Optional[AnyUrl] = None
    statuses_url: Optional[AnyUrl] = None
    head: Optional[Head4] = None
    base: Optional[Base6] = None
    links: Optional[Links5] = Field(None, alias="_links")
    author_association: Optional[AuthorAssociation] = None
    auto_merge: Optional[AutoMerge] = None
    active_lock_reason: Optional[ActiveLockReason] = None
    draft: Optional[bool] = Field(
        None, description="Indicates whether or not the pull request is a draft."
    )
    merged: Optional[bool] = None
    mergeable: Optional[bool] = None
    rebaseable: Optional[bool] = None
    mergeable_state: Optional[str] = None
    merged_by: Optional[User] = None
    comments: Optional[int] = None
    review_comments: Optional[int] = None
    maintainer_can_modify: Optional[bool] = Field(
        None, description="Indicates whether maintainers can modify the pull request."
    )
    commits: Optional[int] = None
    additions: Optional[int] = None
    deletions: Optional[int] = None
    changed_files: Optional[int] = None


class DeploymentProtectionRuleRequested(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["requested"]] = None
    environment: Optional[str] = Field(
        None,
        description="The name of the environment that has the deployment protection rule.",
    )
    event: Optional[str] = Field(
        None, description="The event that triggered the deployment protection rule."
    )
    deployment_callback_url: Optional[AnyUrl] = Field(
        None, description="The URL to review the deployment protection rule."
    )
    deployment: Optional[Deployment] = None
    pull_requests: Optional[List[PullRequest]] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class DeploymentProtectionRuleEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[DeploymentProtectionRuleRequested] = None


class IssueModel(Issue):
    model_config = ConfigDict(extra="allow")
    assignee: Optional[User] = None
    state: Optional[State6] = Field(
        None, description="State of the issue; either 'open' or 'closed'"
    )
    locked: Optional[bool] = None
    labels: Optional[List[Label]] = None


class IssueCommentCreated(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["created"]] = None
    issue: Optional[IssueModel] = Field(
        None,
        description="The [issue](https://docs.github.com/en/rest/reference/issues) the comment belongs to.",
    )
    comment: Optional[IssueComment] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Issue1(IssueModel):
    pass


class IssueCommentDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    issue: Optional[Issue1] = Field(
        None,
        description="The [issue](https://docs.github.com/en/rest/reference/issues) the comment belongs to.",
    )
    comment: Optional[IssueComment] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Issue2(IssueModel):
    pass


class IssueCommentEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    changes: Optional[Changes6] = Field(None, description="The changes to the comment.")
    issue: Optional[Issue2] = Field(
        None,
        description="The [issue](https://docs.github.com/en/rest/reference/issues) the comment belongs to.",
    )
    comment: Optional[IssueComment] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class IssueCommentEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[(IssueCommentCreated, IssueCommentDeleted, IssueCommentEdited)]
    ] = None


class IssuesAssigned(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["assigned"]] = Field(
        None, description="The action that was performed."
    )
    issue: Optional[Issue] = None
    assignee: Optional[User] = Field(
        None,
        description="The optional user who was assigned or unassigned from the issue.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Issue3(Issue):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["closed"]] = None
    closed_at: Optional[str] = None


class IssuesClosed(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["closed"]] = Field(
        None, description="The action that was performed."
    )
    issue: Optional[Issue3] = Field(
        None,
        description="The [issue](https://docs.github.com/en/rest/reference/issues) itself.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class IssuesDeleted(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["deleted"]] = None
    issue: Optional[Issue] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Issue4(Issue):
    model_config = ConfigDict(extra="allow")
    milestone: None = None


class IssuesDemilestoned(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["demilestoned"]] = None
    issue: Optional[Issue4] = None
    milestone: Optional[Milestone] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class IssuesEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    issue: Optional[Issue] = None
    label: Optional[Label] = None
    changes: Optional[Changes7] = Field(None, description="The changes to the issue.")
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class IssuesLabeled(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["labeled"]] = None
    issue: Optional[Issue] = None
    label: Optional[Label] = Field(
        None, description="The label that was added to the issue."
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Issue5(Issue):
    model_config = ConfigDict(extra="allow")
    locked: Optional[Literal[True]] = None
    active_lock_reason: Optional[ActiveLockReason] = None


class IssuesLocked(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["locked"]] = None
    issue: Optional[Issue5] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Issue6(Issue):
    model_config = ConfigDict(extra="allow")
    milestone: Optional[Milestone] = None


class IssuesMilestoned(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["milestoned"]] = None
    issue: Optional[Issue6] = None
    milestone: Optional[Milestone] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Changes8(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    old_issue: Optional[Issue] = None
    old_repository: Optional[Repository] = None


class Issue7(Issue):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["open"]] = None
    closed_at: None = None


class IssuesOpened(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["opened"]] = None
    changes: Optional[Changes8] = None
    issue: Optional[Issue7] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class IssuesPinned(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["pinned"]] = None
    issue: Optional[Issue] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Issue8(Issue):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["open"]] = None


class IssuesReopened(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["reopened"]] = None
    issue: Optional[Issue8] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Changes9(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    new_issue: Optional[Issue] = None
    new_repository: Optional[Repository] = None


class IssuesTransferred(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["transferred"]] = None
    changes: Optional[Changes9] = None
    issue: Optional[Issue] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class IssuesUnassigned(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unassigned"]] = Field(
        None, description="The action that was performed."
    )
    issue: Optional[Issue] = None
    assignee: Optional[User] = Field(
        None,
        description="The optional user who was assigned or unassigned from the issue.",
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class IssuesUnlabeled(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unlabeled"]] = None
    issue: Optional[Issue] = None
    label: Optional[Label] = Field(
        None, description="The label that was removed from the issue."
    )
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class Issue9(Issue):
    model_config = ConfigDict(extra="allow")
    locked: Optional[Literal[False]] = None
    active_lock_reason: None = None


class IssuesUnlocked(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unlocked"]] = None
    issue: Optional[Issue9] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class IssuesUnpinned(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unpinned"]] = None
    issue: Optional[Issue] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class IssuesEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
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
            )
        ]
    ] = None


class PullRequestAssigned(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["assigned"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest] = None
    assignee: Optional[User] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestAutoMergeDisabled(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["auto_merge_disabled"]] = None
    number: Optional[int] = None
    pull_request: Optional[PullRequest] = None
    reason: Optional[str] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestAutoMergeEnabled(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["auto_merge_enabled"]] = None
    number: Optional[int] = None
    pull_request: Optional[PullRequest] = None
    reason: Optional[str] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequest1(PullRequest):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["closed"]] = Field(
        None, description="State of this Pull Request. Either `open` or `closed`."
    )
    closed_at: Optional[datetime] = None
    merged: Optional[bool] = None


class PullRequestClosed(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["closed"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest1] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequest2(PullRequest):
    model_config = ConfigDict(extra="allow")
    closed_at: None = None
    merged_at: None = None
    draft: Optional[Literal[True]] = Field(
        None, description="Indicates whether or not the pull request is a draft."
    )
    merged: Optional[Literal[False]] = None
    merged_by: None = None


class PullRequestConvertedToDraft(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["converted_to_draft"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest2] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequest3(PullRequest):
    model_config = ConfigDict(extra="allow")
    milestone: Optional[Milestone] = None


class PullRequestDemilestoned(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["demilestoned"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest3] = None
    milestone: Optional[Milestone] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class PullRequestDequeued(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["dequeued"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    reason: Optional[str] = Field(
        None, description="The reason the pull request was removed from a merge queue."
    )
    pull_request: Optional[PullRequest] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestEdited(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["edited"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    changes: Optional[Changes25] = Field(
        None, description="The changes to the comment if the action was `edited`."
    )
    pull_request: Optional[PullRequest] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestEnqueued(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["enqueued"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestLabeled(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["labeled"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest] = None
    label: Optional[Label] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestLocked(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["locked"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestMilestoned(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["milestoned"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest3] = None
    milestone: Optional[Milestone] = None
    repository: Optional[Repository] = None
    sender: Optional[User] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None


class PullRequest5(PullRequest):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["open"]] = None
    closed_at: None = None
    merged_at: None = None
    active_lock_reason: None = None
    merged_by: None = None


class PullRequestOpened(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["opened"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest5] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequest6(PullRequest):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["open"]] = None
    closed_at: None = None
    merged_at: None = None
    draft: Optional[Literal[False]] = Field(
        None, description="Indicates whether or not the pull request is a draft."
    )
    merged: Optional[bool] = None
    merged_by: None = None


class PullRequestReadyForReview(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["ready_for_review"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest6] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequest7(PullRequest):
    model_config = ConfigDict(extra="allow")
    state: Optional[Literal["open"]] = None
    closed_at: None = None
    merged_at: None = None
    merged: Optional[bool] = None
    merged_by: None = None


class PullRequestReopened(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["reopened"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest7] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestReviewRequestRemovedItem(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["review_request_removed"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest] = None
    requested_reviewer: Optional[User] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestReviewRequestRemovedItem1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["review_request_removed"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest] = None
    requested_team: Optional[Team] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestReviewRequestRemoved(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (PullRequestReviewRequestRemovedItem, PullRequestReviewRequestRemovedItem1)
        ]
    ] = Field(None, title="pull_request review_request_removed event")


class PullRequestReviewRequestedItem(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["review_requested"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest] = None
    requested_reviewer: Optional[User] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestReviewRequestedItem1(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["review_requested"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest] = None
    requested_team: Optional[Team] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestReviewRequested(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[(PullRequestReviewRequestedItem, PullRequestReviewRequestedItem1)]
    ] = Field(None, title="pull_request review_requested event")


class PullRequestSynchronize(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["synchronize"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    before: Optional[str] = None
    after: Optional[str] = None
    pull_request: Optional[PullRequest] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestUnassigned(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unassigned"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest] = None
    assignee: Optional[User] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestUnlabeled(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unlabeled"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest] = None
    label: Optional[Label] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestUnlocked(GhWebhooksModel):
    model_config = ConfigDict(extra="allow")
    action: Optional[Literal["unlocked"]] = None
    number: Optional[int] = Field(None, description="The pull request number.")
    pull_request: Optional[PullRequest] = None
    repository: Optional[Repository] = None
    installation: Optional[InstallationLite] = None
    organization: Optional[Organization] = None
    sender: Optional[User] = None


class PullRequestEvent(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                PullRequestAssigned,
                PullRequestAutoMergeDisabled,
                PullRequestAutoMergeEnabled,
                PullRequestClosed,
                PullRequestConvertedToDraft,
                PullRequestDemilestoned,
                PullRequestDequeued,
                PullRequestEdited,
                PullRequestEnqueued,
                PullRequestLabeled,
                PullRequestLocked,
                PullRequestMilestoned,
                PullRequestOpened,
                PullRequestReadyForReview,
                PullRequestReopened,
                PullRequestReviewRequestRemoved,
                PullRequestReviewRequested,
                PullRequestSynchronize,
                PullRequestUnassigned,
                PullRequestUnlabeled,
                PullRequestUnlocked,
            )
        ]
    ] = None


class Model(RootModel):
    model_config = ConfigDict(extra="allow")
    root: Optional[
        Union[
            (
                BranchProtectionRuleEvent,
                CheckRunEvent,
                CheckSuiteEvent,
                CodeScanningAlertEvent,
                CommitCommentEvent,
                CreateEvent,
                DeleteEvent,
                DependabotAlertEvent,
                DeployKeyEvent,
                DeploymentEvent,
                DeploymentProtectionRuleEvent,
                DeploymentStatusEvent,
                DiscussionEvent,
                DiscussionCommentEvent,
                ForkEvent,
                GithubAppAuthorizationEvent,
                GollumEvent,
                InstallationEvent,
                InstallationRepositoriesEvent,
                InstallationTargetEvent,
                IssueCommentEvent,
                IssuesEvent,
                LabelEvent,
                MarketplacePurchaseEvent,
                MemberEvent,
                MembershipEvent,
                MergeGroupEvent,
                MetaEvent,
                MilestoneEvent,
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
                RegistryPackageEvent,
                ReleaseEvent,
                RepositoryEvent,
                RepositoryDispatchEvent,
                RepositoryImportEvent,
                RepositoryVulnerabilityAlertEvent,
                SecretScanningAlertEvent,
                SecretScanningAlertLocationEvent,
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
        ]
    ] = None
