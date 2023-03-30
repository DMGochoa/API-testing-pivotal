@workspaces @api
Feature: Workspace
    As an application developer,
    I want to manage pivotal workspaces through REST API,
    So that my app can get answers and show them.

    @Functional @tc_41 @delete_workspace
    Scenario: Create workspace
        Given the user sets the following body parameters
            | name      |
            | workspace |
        When the user sends a "POST" request to "/my/workspaces" endpoint
        Then the response status code should be "200"
        And the response body should contain the following data:
            | kind      | name      |
            | workspace | workspace |
        And the response should fit the following schema "post_workspace_schema.json"