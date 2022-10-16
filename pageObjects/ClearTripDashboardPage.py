import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ClearTripDashboardPage:

    def __init__(self, driver):
        self.driver = driver

    srch_flight_btn = (By.CSS_SELECTOR, ".fw-600.fs-4.lh-2.flex.flex-middle")
    validation_msg = (By.XPATH, "//span[@class='fw-500 fs-2 ml-4']")
    where_from = (By.XPATH, "//input[@placeholder='Where from?']")
    where_to = (By.XPATH, "//input[@placeholder='Where to?']")
    dest_from_results = (By.XPATH, "//ul[@class='airportList']")
    return_date_selector = (By.XPATH, "//div[normalize-space()='Return']//parent::button")
    datepicker = (By.XPATH, "//div[@class='DayPicker w-100p']")
    todays_date = (By.XPATH, "//div[@class='DayPicker-Day DayPicker-Day--start DayPicker-Day--end DayPicker-Day--selected DayPicker-Day--today']//div//div")
    current_date_xpath = "(//div[contains(@class,'DayPicker-Day') and contains(@aria-disabled,'false')]//div//div)[1]"
    future_date = (By.XPATH, "(//div[contains(@class,'DayPicker-Day') and contains(@aria-disabled,'false')]//div//div)[15]")

    def srchflight(self):
        return self.driver.find_element(*ClearTripDashboardPage.srch_flight_btn)

    def get_validation_msg(self):
        return self.driver.find_element(*ClearTripDashboardPage.validation_msg).text

    def dest_where_from(self):
        return self.driver.find_element(*ClearTripDashboardPage.where_from)

    def dest_where_to(self):
        return self.driver.find_element(*ClearTripDashboardPage.where_to)

    def wait_for_resultset(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_all_elements_located(ClearTripDashboardPage.dest_from_results))

    def click_return(self):
        return self.driver.find_element(*ClearTripDashboardPage.return_date_selector)

    def wait_for_datepicker(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(ClearTripDashboardPage.datepicker))

    def get_todays_date(self):
        return self.driver.find_element(*ClearTripDashboardPage.todays_date).text

    def click_future_date(self):
        todays_date = self.driver.find_element(By.XPATH, "//div[contains(@class,'DayPicker-Day') and contains(@aria-disabled,'false')]//div//div").text
        temp_date = todays_date.split("\n")
        current_date = int(temp_date[0])
        print(current_date)
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        self.driver.find_element(*ClearTripDashboardPage.future_date).click()
