""" Conftest file for pytest bdd"""
from main.core.utils.logger import logging
from main.core.api.request_manager import RequestManager


def pytest_bdd_after_scenario(request, scenario):
    """ pytest bdd after scenario

    Args:
        request (object): request object of fixture
        scenario (object): scenario object of pytest bdd
    """
    # pylint: disable=import-error
    tags = scenario.tags
    logging.info(f"Verifing the tags: {tags}")
    # Search for the tag delete
    for tag in tags:
        if 'delete' in tag:
            # Search for the tag project and if matches delete the project
            if 'project' in tag:
                logging.info("Deleting the project")
                req_manager = RequestManager.get_instance()
                id_project = request.response.json()["id"]
                endpoint = f'/projects/{id_project}'
                req_manager.make_request(
                    http_method='DELETE',
                    endpoint=endpoint
                )
                status = req_manager.response.status_code
                logging.info(
                    f"Response for delete: {status}")