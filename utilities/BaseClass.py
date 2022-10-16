import inspect
import logging

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.select import Select
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def go_to_cleartrip(self):
        self.driver.get("https://www.cleartrip.com/")

    def waitforpageload(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//div[@class='flex flex-around ml-6 bg-primary-500 hover:bg-primary-600 c-white bc-transparent c-pointer w-100p py-2 px-5 h-10 fs-4 fw-600 t-all button bs-solid tp-color td-500 bw-1 br-4 lh-solid box-border home-search-btn ml-2--xs']")))
            signup_popup = self.driver.find_element(By.XPATH, "//div[@class='d-flex']").is_displayed()
            if signup_popup == True:
                self.driver.find_element(By.XPATH, "//body/div[@class='p-fixed l-0 r-0 b-0 t-0 flex flex-center flex-middle z-70']/div/div[@class='d-flex']/div[2]/div[1]/div[1]/div[2]//*[name()='svg']").click()
            else:
                pass
        except Exception as e:
            print(e, "page did not load successfully")

