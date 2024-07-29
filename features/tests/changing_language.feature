# Created by Nandini at 7/17/2024
Feature: Task4_Changing language Verifying test

  Scenario: User can change the language from the page
  Given Open the main page
  When  Log in to the page
  Then  Click on Continue button
  Then  Click on Main-menu at the left side menu
  Then  Change the language of the page to Russian
  Then  Verify the language has changed
    #The option will be “RU” which is the list of the languages