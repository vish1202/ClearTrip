import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="V:/Python/Scripts/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="V:/Python/Scripts/geckodriver")
    elif browser_name == "IE":
        driver = webdriver.Ie(executable_path="")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
