from selenium.webdriver.common.by import By
from behave import given, when, then


@Then('Cart Empty is Shown')
def cart_empty(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//*[@class='a-row sc-your-amazon-cart-is-empty']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
