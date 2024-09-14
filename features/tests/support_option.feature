
Feature: Verify support page User can access Whatsapp and Telegram communities


  Scenario: User can access Whatsapp and Telegram communities
    Given Open the main page
    When  Log in to the page
    Then  Click on Continue button
    Then  Click on settings option
    Then  Click on support option
    Then  Switch to the new tab
    Then  Verify the right support page opens
    Then  Go back
    Then  Click on news option
    Then  Verify the right news page opens

  ##(The link contains “api.whatsapp.com”). Don’t click on “Continue to Chat”##
   ##(The link contains “t.me”). Don’t click on “view in telegram”
  ##Please note that in steps 6 and 8 must not click in the options to join Whatsapp and Telegram groups.+
