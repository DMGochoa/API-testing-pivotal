""" Conftest file for pytest bdd"""
# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=ungrouped-imports
from main.core.utils.logger import logging
from tests.utils.hook_create import create_feature
from tests.utils.hook_names import delete_everything
from main.core.api.request_manager import RequestManager

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
            # Search for the tag project and if matches creates
            # the project, stories or workspace
            create_feature(tag, req_manager, request)


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
