from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Sign in page is shown')
def verify_signin_page(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'


