
Feature: Verifying all the cards added in "want to buy" option


  Scenario: User can filter the Secondary deals by “want to buy” option
      Given  Open the main page
      When  Log in to the page
      Then  Click on Continue button
      Then  Click on Secondary option at the left side menu
      Then  Verify Secondary page opens
      Then  Click on Filters
      Then  the products by “want to buy”
      Then  Click on Apply Filter
      Then  Verify all cards have “Want to buy” tag