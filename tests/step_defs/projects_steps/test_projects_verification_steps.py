""" Module that contains the step definitions for the projects verification
"""
from sttable import parse_str_table
from pytest_bdd import then, parsers
# pylint: disable=import-error
from main.core.utils.logger import logging
from main.pivotal.utils.verify_response import VerifyResponse
# pylint: enable=import-error


@then('the response status should be {string}')
@then(parsers.parse('the response status should be "{statuscode}"'))
def validate_status_code(request, statuscode):
    """Validate the status code of the response against the expected one.

    Args:
        request (fixture): Fixture that contains the response and
        is an element from pytest_bdd
        statuscode (str): Status code expected.
    """
    logging.info(
        "Validating the status code the response status should" +
        f"be {statuscode} and is {request.response.status_code}"
    )
    result = request.response.status_code == int(statuscode)
    assert result


@then('the response body should contain the following data')
@then(parsers.parse(
    "the response body should contain the following data\n{body_parameters}"))
def body_params(request, body_parameters):
    """Validate the response body against the expected data.

    Args:
        request (fixture): Fixture that contains the response and
        is an element from pytest_bdd
        body_parameters (dict): Dictionary with the expected data
        of the body.
    """
    logging.info("Validating the response body")
    body_parameters = parse_str_table(body_parameters)
    body_parameters = body_parameters.rows[0]
    logging.info(f"Validating the response body: {body_parameters}")
    for key, value in body_parameters.items():
        result = request.response.json().get(key) == value
        assert result


@then('the response should fit the following schema {string}')
@then(parsers.parse('the response should fit the following schema "{schema}"'))
def validate_schema(request, schema):
    """Validate the response against a schema.

    Args:
        request (fixture): Fixture that contains the response and
        is an element from pytest_bdd
        schema (str): name of the schema.json to validate the response.
    """
    logging.info(f"Validating the response against {schema} schema")
    schema_resp = request.response.json()
    veredict, emsg = VerifyResponse.verify_schema(response=schema_resp,
                                                  schema=schema)
    logging.info(f"Veredict: {veredict} with message: {emsg}")
    assert veredict
