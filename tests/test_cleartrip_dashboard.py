from utilities.BaseClass import BaseClass
from pageObjects.ClearTripDashboardPage import ClearTripDashboardPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestClearTrip(BaseClass):

    def test_verifytitle(self):
        self.go_to_cleartrip()
        self.waitforpageload()
        assert self.driver.title == "Cleartrip: #1 Site for Booking Flights Tickets & Hotels Online - Get Best Travel Deals"

    def test_dest_fieldvalidation(self):
        self.go_to_cleartrip()
        self.waitforpageload()
        ClearTripDashboardPage.srchflight(self).click()
        actual_msg = ClearTripDashboardPage.get_validation_msg(self)
        assert actual_msg == "Enter departure and arrival airports / cities"

    def test_search_flights(self):
        self.go_to_cleartrip()
        self.waitforpageload()
        ClearTripDashboardPage.dest_where_from(self).send_keys("Banga")
        ClearTripDashboardPage.wait_for_resultset(self)
        from_results = self.driver.find_elements(*ClearTripDashboardPage.dest_from_results)
        from_results[0].click()
        ClearTripDashboardPage.dest_where_to(self).send_keys("Delhi")
        ClearTripDashboardPage.wait_for_resultset(self)
        to_results = self.driver.find_elements(*ClearTripDashboardPage.dest_from_results)
        to_results[0].click()
        ClearTripDashboardPage.click_return(self).click()
        ClearTripDashboardPage.wait_for_datepicker(self)
        ClearTripDashboardPage.click_future_date(self)
        ClearTripDashboardPage.srchflight(self).click()
