# Created by roya at 9/30/22
Feature: Test to see the cart
  # Enter feature description here

  Scenario: User can see that the cart is empty
     Given Open Amazon Page
     When Find Cart
     Then Cart Empty is Shown