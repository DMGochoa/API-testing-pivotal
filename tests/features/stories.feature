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