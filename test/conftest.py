import pytest
from selenium import webdriver
import time
driver = None

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        s = Service("c:\\Users/masca/Chromedriver/chromedriver")
        driver = webdriver.Chrome(service=s)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    #elif browser_name == "firefox":
     #   driver = webdriver.Firefox(executable_path="c:\\Users/masca/Downloads/Geckodriver/geckodriver")
                #elif browser_name == "ie"
        #print("IE driver")      #ie driver invocation
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


