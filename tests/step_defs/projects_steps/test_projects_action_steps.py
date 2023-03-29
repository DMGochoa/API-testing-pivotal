"""This module contains the step definitions for the projects feature
"""
# pylint: disable=import-error
from sttable import parse_str_table
from pytest_bdd import given, when, parsers
from main.core.utils.logger import logging
from main.core.api.request_manager import RequestManager


@given('the user sets the following body parameters')
@given(parsers.parse(
    "the user sets the following" +
    " body parameters\n{body_parameters}"
))
def set_body_parameters(request, body_parameters):
    """This function sets the body parameters"""
    body_parameters = parse_str_table(body_parameters)
    body_parameters = body_parameters.rows[0]
    logging.info(f"Setting the body parameters: {body_parameters}")
    request.params = body_parameters


@when('the user sends a {string} request to {string} endpoint')
@when(parsers.parse(
    'the user sends a "{httpmethod}" request to "{endpoint}" endpoint'))
def send_request(request, httpmethod, endpoint):
    """This function sends a request"""
    logging.info(f"Sending a request {httpmethod} to {endpoint} endpoint")
    req_manager = RequestManager.get_instance()
    request.response = req_manager.make_request(http_method=httpmethod,
                                                endpoint=endpoint,
                                                payload=request.params)
    logging.info(f"Response: {request.response.json()}")
