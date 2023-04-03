@stories @api
Feature: Stories
    As an aplication developer, I want
    to work with stories in Pivotal Tracker
    so that I can start working with Stories on my Project.

    @functional @tc_21 @create_project @delete_project
    Scenario: Create a story
        Given the user sets the following body parameters
            | name         | story_type  | description            |
            | New-story    | feature     | This is a new story    |
        When the user sends a "POST" request to "/projects/<projects.id>/stories" endpoint
        Then the response status code should be "200"
        And the response body should contain the following data
            | name         | story_type  | description            |
            | New-story    | feature     | This is a new story    |
        And the response should fit the following schema "post_stories_schema.json"

    @smoke @tc_22 @create_project @delete_project @create_stories
    Scenario: Return all Stories from a Project
        When the user sends a "GET" request to "/projects/<projects.id>/stories" endpoint
        Then the response status code should be "200"
        And the response body should contain a list of "3" stories associated with the project
        And the response should fit the following schema "get_stories_schema.json"

    @functional @tc_23 @create_project @create_story @delete_project
    Scenario: Update a story
        Given the user sets the following body parameters
            | name            | story_type  | description                |
            | Updated-story   | feature     | This is a Updated story    |
        When the user sends a "PUT" request to "/projects/<projects.id>/stories/<stories.id>" endpoint
        Then the response status code should be "200"
        And the response body should contain the following data
            | name            | story_type  | description                |
            | Updated-story   | feature     | This is a Updated story    |
        And the response should fit the following schema "post_stories_schema.json"

    @functional @tc_24 @create_project @create_story @delete_project
    Scenario: Delete a story
        When the user sends a "DELETE" request to "/projects/<projects.id>/stories/<stories.id>" endpoint
        Then the response status code should be "204"
        And the items from "/projects/<projects.id>/stories" should have "0" elements

    @smoke @tc_25 @create_project @delete_project
    Scenario: Search for projects when there are no records
        When the user sends a "GET" request to "//projects/<projects.id>/stories" endpoint
        Then the response status code should be "200"
        And the response body should have "0" elements
        And the response should fit the following schema "get_stories_schema.json"
