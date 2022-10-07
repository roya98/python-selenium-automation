from selenium.webdriver.common.by import By
from behave import given, when, then

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME =(By.ID, 'productTitle')

@given('Open Amazon Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Find returns & orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(product)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()





