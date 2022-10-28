from selenium.webdriver.common.by import By
from behave import given, when, then


PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")




@when('Open cart page')
def open_cart_page(context):
   # context.driver.get("https://www.amazon.com/gp/cart/view.html?ref_=nav_cart")
      context.app.cart_page.open_url('/gp/cart/view.html?ref_=nav_cart')

@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    # actual_text = context.driver.find_element(*CART).text
    # assert expected_count == actual_text, f'Expected {expected_count} but got {actual_text}'
       context.app.cart_page.check_cart_count(expected_count)

@then('Verify cart has correct product')
def verify_product_name(context):
 actual_name = context.driver.find_element(*PRODUCT_NAME).text
 assert context.product_name[:30] in actual_name, f'Expected {context.product_name}, but got {actual_name}'


@then('Cart Empty is Shown')
def cart_empty(context):
    context.app.cart_page.cart_empty_check()