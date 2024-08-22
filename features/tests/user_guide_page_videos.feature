
Feature: Task7 Verify User Guide page

  Scenario: User can open User guide page
    Given Open the main page
    When  Log in to the page
    Then  Click on the continue button
    Then  Click on settings option
    Then  Click on User Guide option
    Then  Verify right page tab opens
    Then  Verify all lesson videos contain titles
    