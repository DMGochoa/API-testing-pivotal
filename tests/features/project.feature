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
