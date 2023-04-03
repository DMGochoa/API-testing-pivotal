@projects @api
Feature: Project
    As an aplication developer, I want
    to work with project in Pivotal Tracker
    so that I can start tracking my work.

    @functional @tc_01 @delete_project
    Scenario: Create a project
        Given the user sets the following body parameters
            | name         | description            |
            | My-Project   | My Project Description |
        When the user sends a "POST" request to "/projects" endpoint
        Then the response status code should be "200"
        And the response body should contain the following data
            | name         | description            |
            | My-Project   | My Project Description |
        And the response should fit the following schema "post_project_schema.json"
    
    @smoke @tc_02
    Scenario: Search for projects when there are no records
        When the user sends a "GET" request to "/projects" endpoint
        Then the response status code should be "200"
        And the response body should have "0" elements
        And the response should fit the following schema "get_projects_schema.json"
    
    @functional @tc_03 @create_project @delete_project @negative
    Scenario: A project can't be creted with a duplicated name
        Given the user sets the following body parameters
            | name         | description            |
            | My-Project   | My Project Description |
        When the user sends a "POST" request to "/projects" endpoint
        Then the response status code should be "400"
        And the response body should contain the following data
            | code                | kind  |
            | invalid_parameter   | error |
        And the response should fit the following schema "post_project_schema.json"

    @functional @tc_04 @create_project @delete_project
    Scenario: Project can be updated
        Given the user sets the following body parameters
            | name               | description                   |
            | My-Project-update  | My Project update Description |
        When the user sends a "PUT" request to "/projects/<projects.id>" endpoint
        Then the response status code should be "200"
        And the response body should contain the following data
            | name               | description                   |
            | My-Project-update  | My Project update Description |
        And the response should fit the following schema "put_specific_project_schema.json"
