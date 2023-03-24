""" Module for the constants normally used for the Pivotal API.
"""
from enum import Enum


class PivotalApiEndpoints(Enum):
    """ Enum for the Pivotal API endpoints.
    """
    PROJECTS = 'projects'
    PROJECT = 'projects/{}'
    PROJECT_MEMBERSHIPS = 'projects/{}/memberships'
    PROJECT_MEMBERSHIP = 'projects/{}/memberships/{}'
    PROJECT_MEMBERSHIP_BY_USER = 'projects/{}/memberships?' \
        + 'person_id={}'
    PROJECT_MEMBERSHIP_BY_USER_AND_PROJECT = 'projects/{}/' \
        + 'memberships?person_id={}'

    PROJECT_MEMBERS = 'projects/{}/members'
    PROJECT_MEMBER = 'projects/{}/members/{}'

    PROJECT_STORIES = 'projects/{}/stories'
    PROJECT_STORY = 'projects/{}/stories/{}'
    PROJECT_STORY_COMMENTS = 'projects/{}/stories/{}/comments'
    PROJECT_STORY_COMMENT = 'projects/{}/stories/{}/comments/{}'
    PROJECT_STORY_TASKS = 'projects/{}/stories/{}/tasks'
    PROJECT_STORY_TASK = 'projects/{}/stories/{}/tasks/{}'

    PROJECT_LABELS = 'projects/{}/labels'
    PROJECT_LABEL = 'projects/{}/labels/{}'
    PROJECT_LABEL_STORIES = 'projects/{}/labels/{}/stories'
    PROJECT_LABEL_STORY = 'projects/{}/labels/{}/stories/{}'

    PROJECT_WEBHOOKS = 'projects/{}/webhooks'
    PROJECT_WEBHOOK = 'projects/{}/webhooks/{}'

    PROJECT_ACTIVITY = 'projects/{}/activity'
    PROJECT_ACTIVITY_STORY = 'projects/{}/activity?event_' \
        + 'type=story_update_activity'
    PROJECT_ACTIVITY_STORY_CREATE = 'projects/{}/activity?' \
        + 'event_type=story_create_activity'
    PROJECT_ACTIVITY_STORY_DELETE = 'projects/{}/activity?' \
        + 'event_type=story_delete_activity'
    PROJECT_ACTIVITY_COMMENT = 'projects/{}/activity?event_' \
        + 'type=comment_create_activity'
    PROJECT_ACTIVITY_COMMENT_DELETE = 'projects/{}/activity?' \
        + 'event_type=comment_delete'
