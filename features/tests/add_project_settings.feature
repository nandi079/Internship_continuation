Feature: AQA_task5 test_cases setting through project

  Scenario: User can add a project through the settings
    Given Open the main page
    When  Log in to the page
    Then  Click on the continue button
    Then  Click on settings option
    Then  Click on Add a project
    Then  Verify the right page opens
    Then  Add some test information to the input fields
    Then  Verify the right information is present in the input fields
    Then  Verify “Send an application” button is available and clickable
