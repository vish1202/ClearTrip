from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

    srch_results = (By.XPATH, "//div[contains(@class,'ba bc-neutral-100')]")
    book_btn = (By.XPATH, "//button[contains(@class,'bg-primary-500')]")

    def wait_for_search_results(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(SearchResultsPage.srch_results))

    def click_book_btn(self):
        self.driver.find_element(*SearchResultsPage.book_btn).click()
