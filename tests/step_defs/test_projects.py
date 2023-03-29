"""
This module contains the step definitions for the projects feature.
"""
import os
# pylint: disable=import-error
from pytest_bdd import scenario
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=line-too-long
from main.core.utils.logger import logging
from tests.step_defs.projects_steps.test_projects_action_steps import *  # noqa: F403,F401,E501
from tests.step_defs.projects_steps.test_projects_verification_steps import *  # noqa: F403,F401,E501
# pylint: enable=import-error
# pylint: enable=wildcard-import
# pylint: enable=unused-wildcard-import
# pylint: enable=line-too-long

logging.info("Executing the projects feature")
feature_path = os.path.join(os.path.dirname(__file__),
                            '..',
                            'features')


@scenario(os.path.join(feature_path, 'project.feature'), 'Create a project')
def test_create_project():
    """
    This function executes the scenarios for the create project feature
    """
    logging.info("Executing scenarios for create project feature")
