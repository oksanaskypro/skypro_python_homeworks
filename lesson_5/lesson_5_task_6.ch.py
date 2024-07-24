from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get ('http://the-internet.herokuapp.com/login')
input_name = driver.find_element (By.ID,'username').send_keys('tomsmith')
input_pass = driver.find_element (By.ID,'password').send_keys('SuperSecretPassword!')
button = driver.find_element (By.TAG_NAME, 'button').click()
sleep(2)
