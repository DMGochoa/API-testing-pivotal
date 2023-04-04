"""This module is for the creation of before features"""
# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=ungrouped-imports
from main.core.utils.logger import logging
from main.core.api.enums.http_methods_enum import HttpMethods
from main.pivotal.api.enums.project_constants import (
    ProjectsEndpoints, WorkspaceEndpoints,
    EndpointTags,
)  # noqa: E501

# pylint: enable=import-error
# pylint: enable=no-name-in-module
# pylint: enable=ungrouped-imports


def send_request(req_manager, endpoint, body_parameters):
    """This function create a request and returns
    the is for the before scenario"""
    response = req_manager.make_request(
        http_method=HttpMethods.POST.value,
        endpoint=endpoint,
        payload=body_parameters,
    )
    status = response.status_code
    logging.info(
        "Response status for the " +
        f"before scenario creation: {status}")
    logging.info(
        "Response for the " +
        f" creation: {req_manager.response}"
    )
    return response.json()["id"]


def create_feature(tag, req_manager, request):
    """This function verify what kind of feature has
    to be created for the before scenario"""
    if "stories" in tag:
        logging.info("Creating the stories")
        project_id_tag = EndpointTags.PROJECT_ID.value
        endpoint = (
            "/projects/" +
            f"{request.before_scenario[project_id_tag]}/stories"
        )
        logging.info(f"TOOO this endpoint: {endpoint}")
        for story_number in range(1, 4):
            body_parameters = {
                "name": f"My-story-{story_number}",
                "description": "A temporal project for"
                + " stories testing purposes",
            }
            response = req_manager.make_request(
                http_method=HttpMethods.POST.value,
                endpoint=endpoint,
                payload=body_parameters,
            )
            status = response.status_code
            logging.info(
                "Response status for the story " +
                f"#{story_number} creation: {status}"
            )
            logging.info(
                "Response for the story"
                + f" #{story_number} creation: {req_manager.response}"
            )
    else:
        if "story" in tag:
            logging.info("Creating the story")
            project_id_tag = EndpointTags.PROJECT_ID.value
            endpoint = (
                "/projects/" +
                f"{request.before_scenario[project_id_tag]}/stories"
            )
            logging.info(f"TOOO this endpoint: {endpoint}")
            body_parameters = {
                "name": "New-story",
                "story_type": "feature",
                "description": "This is a new story "
            }
            id_tag = EndpointTags.STORY_ID.value
        elif "project" in tag:
            logging.info("Creating the project")
            endpoint = ProjectsEndpoints.PROJECTS.value
            body_parameters = {
                "name": "My-Project",
                "description": "A temporal project for"
                + " stories testing purposes",
            }
            id_tag = EndpointTags.PROJECT_ID.value
        elif "workspace" in tag:
            logging.info("Creating the workspace")
            endpoint = WorkspaceEndpoints.WORKSPACES.value
            body_parameters = {
                "name": "My-Workspace"
            }
            id_tag = EndpointTags.WORKSPACE_ID.value
        request.before_scenario[id_tag] = send_request(
            req_manager, endpoint, body_parameters)
