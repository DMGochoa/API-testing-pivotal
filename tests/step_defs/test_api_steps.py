"""
This module contains the step definitions for the projects feature.
"""
import os
from pytest_bdd import scenario
from main.core.utils.logger import logging
from tests.step_defs.workspace_steps.workspace_action_steps import *  # noqa: F403,F401,E501
from tests.step_defs.workspace_steps.workspace_verification_steps import *  # noqa: F403,F401,E501

logging.info("Executing the projects feature")
feature_path = os.path.join(os.path.dirname(__file__),
                            '..',
                            'features')


@scenario(os.path.join(feature_path, 'workspace.feature'), 'Create workspace')
def test_create_workspace():
    """
    This function executes the scenarios for the create project feature
    """
    logging.info("Executing scenarios for create project feature")
