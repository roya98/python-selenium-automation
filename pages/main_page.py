from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    CART_ICON = (By.XPATH, "//span[@class='nav-cart-icon nav-sprite']")

    def open_main(self):
        self.open_url()

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)



    def click_on_cart(self):
        self.driver.find_element(*self.CART_ICON).click()
