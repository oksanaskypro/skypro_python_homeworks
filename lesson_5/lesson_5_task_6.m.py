from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Firefox()
driver.get ('http://the-internet.herokuapp.com/login')
input_name = driver.find_element (By.ID,'username').send_keys('tomsmith')
input_pass = driver.find_element (By.ID,'password').send_keys('SuperSecretPassword!')
button = driver.find_element (By.TAG_NAME, 'button').click()
sleep(2)
