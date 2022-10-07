from selenium.webdriver.common.by import By
from behave import given, when, then

CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")

@Then('Cart Empty is Shown')
def cart_empty(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//*[@class='a-row sc-your-amazon-cart-is-empty']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'


@when('Open cart page')
def open_cart_page(context):
    context.driver.get("https://www.amazon.com/gp/cart/view.html?ref_=nav_cart")


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count} but got {actual_text}'


@then('Verify cart has correct product')
def verify_product_name(context):
 actual_name = context.driver.find_element(*PRODUCT_NAME).text
 assert context.product_name[:30] in actual_name, f'Expected {context.product_name}, but got {actual_name}'


