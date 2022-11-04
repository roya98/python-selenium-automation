from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('Open Amazon Fashion Page')
def open_amazon_fashion(context):
    context.app.amazon_fashion.open_url('/gp/product/B074TBCSC8')


@when('hover over New Arrivals')
def hover_over_new_arrivals(context):
    context.app.amazon_fashion.hover_fashion()


@then('Verify deals')
def verify_deals(context):
    context.app.amazon_fashion.verify_deals()