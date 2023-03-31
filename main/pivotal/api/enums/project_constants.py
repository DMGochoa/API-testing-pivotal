""" Module for the constants normally used for the Pivotal API.
"""
from enum import Enum


class EndpointTags(Enum):
    PROJECT_ID = '<projects.id>'
    MEMBERSHIP_ID = '<membership.id>'
    PERSON_ID = '<person.id>'
    STORY_ID = '<stories.id>'


class ProjectsEndpoints(Enum):
    """ Enum for the Pivotal API endpoints.
    """
    tag_project = EndpointTags.PROJECT_ID.value
    tag_membership = EndpointTags.MEMBERSHIP_ID.value
    tag_person = EndpointTags.PERSON_ID.value
    tag_story = EndpointTags.STORY_ID.value

    PROJECTS = '/projects'
    PROJECT = f'/projects/{tag_project}'
    PROJECT_MEMBERSHIPS = f'/projects/{tag_project}/memberships'
    PROJECT_MEMBERSHIP = f'/projects/{tag_project}' + \
        f'/memberships/{tag_membership}'
    PROJECT_MEMBERSHIP_BY_USER = f'/projects/{tag_project}/memberships?' \
        + f'person_id={tag_person}'
    PROJECT_MEMBERSHIP_BY_USER_AND_PROJECT = f'/projects/{tag_project}/' \
        + f'memberships?person_id={tag_person}'

    PROJECT_MEMBERS = f'/projects/{tag_project}/members'
    PROJECT_MEMBER = f'/projects/{tag_project}/members/<members.id>'

    PROJECT_STORIES = f'/projects/{tag_project}/stories'
    PROJECT_STORY = f'/projects/{tag_project}/stories/{tag_story}'
    PROJECT_STORY_COMMENTS = f'/projects/{tag_project}' + \
        f'/stories/{tag_story}/comments'
    PROJECT_STORY_COMMENT = '/projects/{}/stories/{}/comments/{}'
    PROJECT_STORY_TASKS = '/projects/{}/stories/{}/tasks'
    PROJECT_STORY_TASK = '/projects/{}/stories/{}/tasks/{}'

    PROJECT_LABELS = '/projects/{}/labels'
    PROJECT_LABEL = '/projects/{}/labels/{}'
    PROJECT_LABEL_STORIES = '/projects/{}/labels/{}/stories'
    PROJECT_LABEL_STORY = '/projects/{}/labels/{}/stories/{}'

    PROJECT_WEBHOOKS = '/projects/{}/webhooks'
    PROJECT_WEBHOOK = '/projects/{}/webhooks/{}'

    PROJECT_ACTIVITY = '/projects/{}/activity'
    PROJECT_ACTIVITY_STORY = '/projects/{}/activity?event_' \
        + 'type=story_update_activity'
    PROJECT_ACTIVITY_STORY_CREATE = '/projects/{}/activity?' \
        + 'event_type=story_create_activity'
    PROJECT_ACTIVITY_STORY_DELETE = '/projects/{}/activity?' \
        + 'event_type=story_delete_activity'
    PROJECT_ACTIVITY_COMMENT = '/projects/{}/activity?event_' \
        + 'type=comment_create_activity'
    PROJECT_ACTIVITY_COMMENT_DELETE = '/projects/{}/activity?' \
        + 'event_type=comment_delete'
