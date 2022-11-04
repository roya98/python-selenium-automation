# Created by roya at 11/3/22
Feature: Checking new arrivals
  # Enter feature description here

  Scenario: User can check out the new arrivals
    Given Open Amazon Fashion Page
    When hover over New Arrivals
    Then Verify deals
