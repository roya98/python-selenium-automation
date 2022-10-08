from selenium.webdriver.common.by import By
from behave import given, when, then


LINKS = (By.CSS_SELECTOR, "._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a")

@given('Open Amazon Best Seller')
def open_amazon_bestseller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')



@then('Verify five links')
def verify_links(context):
  links = context.driver.find_elements(*LINKS)
  assert len(links) == 5, f'expected 5 but got {len(links)}'


