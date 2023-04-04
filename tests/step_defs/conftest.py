""" Conftest file for pytest bdd"""
# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=ungrouped-imports
from main.core.utils.logger import logging
from tests.utils.hook_names import delete_everything
from main.core.api.request_manager import RequestManager
from main.core.api.enums.http_methods_enum import HttpMethods
from main.pivotal.api.enums.project_constants import (
    ProjectsEndpoints, WorkspaceEndpoints,
    EndpointTags,
)  # noqa: E501

# pylint: enable=import-error
# pylint: enable=no-name-in-module
# pylint: enable=ungrouped-imports


def pytest_bdd_before_scenario(request, scenario):
    """pytest bdd after scenario

    Args:
        request (object): request object of fixture
        scenario (object): scenario object of pytest bdd
    """
    # pylint: disable=import-error
    tags = sorted(list(scenario.tags))
    logging.info(f"Verifing the tags: {tags}")
    req_manager = RequestManager.get_instance()
    request.before_scenario = {}
    for tag in tags:
        if "create" in tag:
            # Search for the tag project and if matches creates a the project
            # Search for the tag stories and if
            # matches creates stories in a project
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
                response = req_manager.make_request(
                    http_method=HttpMethods.POST.value,
                    endpoint=endpoint,
                    payload=body_parameters,
                )
                request.before_scenario[id_tag] = response.json()["id"]
                status = response.status_code
                logging.info(
                    "Response status for the " +
                    f"before scenario creation: {status}")
                logging.info(
                    "Response for the " +
                    f" creation: {req_manager.response}"
                )


def pytest_bdd_after_scenario(scenario):
    """pytest bdd after scenario

    Args:
        request (object): request object of fixture
        scenario (object): scenario object of pytest bdd
    """
    tags = scenario.tags
    logging.info(f"Tags: {tags}")
    # Search for the tag delete
    for tag in tags:
        if "delete" in tag:
            # Search for the tag story and if matches delete the story
            if "workspace" in tag:
                logging.info("Deleting the workspace")
                delete_everything("/my/workspaces")
            elif "project" in tag:
                logging.info("Start deleting all the projects")
                delete_everything("/projects")

            status = RequestManager.get_instance().response.status_code
            logging.info(f"Response for delete: {status}")
