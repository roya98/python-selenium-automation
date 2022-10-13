# Created by roya at 10/6/22
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can add a product to the cart
    Given Open Amazon Page
    When Search for Dress
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)