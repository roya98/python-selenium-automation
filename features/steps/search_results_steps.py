from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


# $x("//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")




@when('Click on the first product')
def click_first_product(context):
    # context.driver.find_element(*PRODUCT_PRICE).click()
      context.app.search_results_page.click_first_product_check()


@then('Search results for {expected_result} are shown')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'






