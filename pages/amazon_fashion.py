from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Fashion(Page):

    NEW_ARRIVALS = (By.CSS_SELECTOR, '.nav-hasArrow[aria-label="New Arrivals"]')
    # DEALS = (By.ID, 'nav-flyout-abAcquisition')
    DEALS = (By.XPATH, '//a[contains(@href,"/s?i=fashion-womens&bbn=19225926011&r")]')
   # DEALS = (By.XPATH, '//ul[@class="mm-category-list"]/li[h3/text()="Women"]')





    def hover_fashion(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        action = ActionChains(self.driver)
        action.move_to_element(new_arrivals)
        action.perform()
        sleep(10)


    def verify_deals(self):
        self.wait_for_element_appear(*self.DEALS)

