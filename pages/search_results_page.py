from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.SEARCH_RESULTS)


    def click_first_product_check(self):
        self.driver.find_element(*self.PRODUCT_PRICE).click()


