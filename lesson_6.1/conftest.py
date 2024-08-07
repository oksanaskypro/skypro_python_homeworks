import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture ()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window ()
    yield driver
    driver.quit()

