# Created by roya at 9/28/22
Feature: Test to see sign in page
  # Enter feature description here

  Scenario: User can see sign in page when click on orders
    Given Open Amazon Page
    When Find returns & orders
    Then Sign in page is shown
