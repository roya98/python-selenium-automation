from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME =(By.ID, 'productTitle')

HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem a')
SIGN_IN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-button")
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')


@given('Open Amazon Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Find returns & orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_INPUT).send_keys(product)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('Click on button from SignIn popup')
def click_sign_in(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN), message='sign in not clickable')
    e.click()



@then('Verify hamburger menu is present')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)