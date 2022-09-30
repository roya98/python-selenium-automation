from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Find Cart')
def find_cart(context):
    context.driver.find_element(By.XPATH, "//span[@class='nav-cart-icon nav-sprite']").click()



