"""This module is to create a class to obtain the tags creation/delete names"""
# pylint: disable=import-error
# pylint: disable=no-self-argument
from main.core.api.request_manager import RequestManager
from main.core.utils.logger import logging
from main.core.api.enums.http_methods_enum import HttpMethods


def delete_everything(endpoint):
    """This function is to delete everything from a endpoint

    Args:
        endpoint (str): endpoint to delete everything
    """
    logging.info(f"Deleting everything from {endpoint}")
    response = RequestManager.get_instance().make_request(
        http_method=HttpMethods.GET.value,
        endpoint=endpoint
    )
    list_of_objects = response.json()
    if list_of_objects:
        logging.info(f"Response for the get: {list_of_objects}")
        for item in list_of_objects:
            object_id = item["id"]
            logging.info(endpoint + "/" + str(object_id))
            response_del = RequestManager.get_instance().make_request(
                http_method=HttpMethods.DELETE.value,
                endpoint=endpoint + "/" + str(object_id)
            )
            logging.info(
                "Response for the deletion " +
                f"of {object_id}: {response_del.text}")
