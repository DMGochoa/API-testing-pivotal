@workspaces @api
Feature: Workspace
    As an application developer,
    I want to manage pivotal workspaces through REST API,
    So that my app can get answers and show them.

    @functional @tc_41 @delete_workspace
    Scenario: Create workspace
        Given the user sets the following body parameters
            | name      |
            | workspace |
        When the user sends a "POST" request to "/my/workspaces" endpoint
        Then the response status code should be "200"
        And the response body should contain the following data
            | kind      | name      |
            | workspace | workspace |
        And the response should fit the following schema "post_workspace_schema.json"


    @smoke @tc_42 @create_workspace @delete_workspace
    Scenario: Get specific workspace
        When the user sends a "GET" request to "/my/workspaces/<workspace.id>" endpoint
        Then the response status code should be "200"
        And the response body should contain the following data
            | kind      | name            |
            | workspace | My-Workspace    |
        And the response should fit the following schema "post_workspace_schema.json"


    @negative @tc_43
    Scenario: Create workspace without a name
        Given the user sets the following body parameters
            | name      |
            |           |
        When the user sends a "POST" request to "/my/workspaces" endpoint
        Then the response status code should be "400"
        And the response body should contain the following data
            | code              | kind     | general_problem    |
            | invalid_parameter | error    | Name can't be blank|


    @smoke @tc_44
    Scenario: Get all workspaces when there are no records
        When the user sends a "GET" request to "/my/workspaces" endpoint
        Then the response status code should be "200"
        And the response body should have "0" elements
        And the response should fit the following schema "get_workspaces_schema.json"


    @refactor @smoke @tc_45 @create_workspace @delete_workspace
    Scenario: Update the name of a workspace
        Given the user sets the following body parameters
            | name              |
            | updated workspace |
        When the user sends a "PUT" request to "/my/workspaces/<workspace.id>" endpoint 
        Then the response status code should be "400"
        And the response body should contain the following data
            | code              | kind     | general_problem                                 |
            | invalid_parameter | error    | this endpoint cannot accept the parameter: name |


    @functional @tc_46 @create_workspace
    Scenario: Delete a workspace
        When the user sends a "DELETE" request to "/my/workspaces/<workspace.id>" endpoint
        Then the response status code should be "204"
        And the items from "/my/workspaces/" should have "0" elements
    