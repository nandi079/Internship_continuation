
Feature: Verify products price range


  Scenario: User can filter the Secondary deals by Unit price range
    Given Open the main page
    When  Log in to the page
    Then  Click on Continue button
    Then  Click on Secondary option at the left side menu
    Then  Verify the Secondary page opens
    Then  Click on Filters
    Then  Filter the products by price range from 1200000 to 2000000 AED
    Then  Verify the price in all cards is inside the range (1200000 - 2000000)

