
Feature: Verify 12 setting options


  Scenario: User can go to settings and see the right number of UI elements
  Given Open the main page
  When  Log in to the page
  Then  Click on Continue button
  Then  Click on settings option
  Then  Verify right page opening
  Then  Verify there are 12 options for the settings
  Then  Verify “connect the company” button is available