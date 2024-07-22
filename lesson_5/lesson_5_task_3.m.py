from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
driver = webdriver.Firefox()
driver.get ("http://uitestingplayground.com/classattr")
for i in range(3):
    blue_button=driver.find_element (
        "xpath","//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    blue_button.click()
    sleep(2)
    driver.switch_to.alert.accept()

    
