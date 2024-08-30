
Feature: Verify change password without clicking


  Scenario: User can open change password page
    Given Open the main page
    When  Log in to the page
    Then  Click on Continue button
    Then  Click on settings option
    Then  Click on Change password option
    Then  Verify the right page opens as set new password
    Then  Add some test password to the input fields
    Then  Verify the “Change password” button is available
          #(but don’t click on it)