""" Module that contains the step definitions for the workspace verification
"""
# pylint: disable=import-error
from sttable import parse_str_table
from pytest_bdd import then, parsers
from main.core.utils.logger import logging
from main.pivotal.utils.verify_response import VerifyResponse
# pylint: enable=import-error


@then(
    parsers.parse('the response status code should be "{statuscode}"'))
def validate_status_code(request, statuscode):
    """This function validates the status code
        recive the reques fixture
        recieve the statuscode
    """
    logging.info(
        "Validating the status code the response " +
        "status should be {statuscode} and " +
        f"is {request.response.status_code}")
    assert request.response.status_code == int(statuscode)


@then(
    parsers.parse("the response body should contain" +
                  " the following data\n{body_parameters}"))
def body_params(request, body_parameters):
    """This function validates the response body
        recives the request fixture
        recives the body parameters which is a dict
    """
    logging.info("Validating the response body")
    body_parameters = parse_str_table(body_parameters)
    body_parameters = body_parameters.rows[0]
    logging.info(f"Validating the response body: {body_parameters}")
    for key, value in body_parameters.items():
        assert request.response.json().get(key) == value


@then(parsers.parse('the response should fit the following schema "{schema}"'))
def validate_schema(request, schema):
    """This function validates the response body
        recives a request fixture
        recives a schema to validate the response
    """
    logging.info(f"Validating the response against {schema} schema")
    schema_resp = request.response.json()
    veredict, emsg = VerifyResponse.verify_schema(response=schema_resp,
                                                  schema=schema)
    logging.info(f"Veredict: {veredict} with message: {emsg}")
    assert veredict
