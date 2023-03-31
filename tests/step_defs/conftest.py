""" Conftest file for pytest bdd"""
# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=ungrouped-imports
from main.core.utils.logger import logging
from tests.utils.hook_names import delete_everything
from main.core.api.request_manager import RequestManager
from main.core.api.enums.http_methods_enum import HttpMethods
from main.pivotal.api.enums.project_constants import (
    ProjectsEndpoints,
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
    tags = scenario.tags
    logging.info(f"Verifing the tags: {tags}")
    req_manager = RequestManager.get_instance()
    request.before_scenario = {}
    for tag in tags:
        if "create" in tag:
            # Search for the tag project and if matches creates a the project
            if "project" in tag:
                logging.info("Creating the project")
                endpoint = ProjectsEndpoints.PROJECTS.value
                body_parameters = {
                    "name": "My-Project",
                    "description": "A temporal project for"
                    + " stories testing purposes",
                }
                response = req_manager.make_request(
                    http_method=HttpMethods.POST.value,
                    endpoint=endpoint,
                    payload=body_parameters,
                )
                project_id_tag = EndpointTags.PROJECT_ID.value
                request.before_scenario[project_id_tag] = response.json()["id"]
                status = response.status_code
                logging.info(
                    f"Response status for the project creation: {status}"
                )
                logging.info(
                    "Response for the project" +
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
