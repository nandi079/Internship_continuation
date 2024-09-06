
Feature: Verify "Subscription & payments" page


  Scenario: User can open Subscription & payments page
  Given Open the main page
  When  Log in to the page
  Then  Click on Continue button
  Then  Click on settings option
  Then  Click on Subscription & payments option
  Then  Verify the accurate page opens
  Then  Verify title “Subscription & payments” is visible
  Then  Verify “upgrade plan” and "back" buttons are available
