from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configuration import *
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def task_data_types_form (chrome_browser):
    chrome_browser.get(URL_1)
    chrome_browser.find_element(By.NAME, "First_name").send_keys(First_name)
    chrome_browser.find_element(By.NAME, "Last_name").send_keys(Last_name)
    chrome_browser.find_element(By.NAME, "Address").send_keys(Address)
    chrome_browser.find_element(By.NAME, "Email").send_keys(Email)
    chrome_browser.find_element(By.NAME, "Phone_number").send_keys(Phone_number)
    chrome_browser.find_element(By.NAME, "Zip_code").send_keys(Zip_code)
    chrome_browser.find_element(By.NAME, "City").send_keys(City)
    chrome_browser.find_element(By.NAME, "Country").send_keys (Country)
    chrome_browser.find_element(By.NAME, "Job_position").send_keys(Job_position)
    chrome_browser.find_element(By.NAME, "Company").send_keys(Company)

    WebDriverWait (chrome_browser, 40, 0.1).until (EC.element_to_be_clickable ((By.TAG_NAME,"button"))).click()
    assert 'danger' in chrome_browser (By. ID,'Zip_code').get_attribute('class')
    assert 'success' in chrome_browser.find_element (By.ID, 'First_name').get_attribute('class')
    assert 'success' in chrome_browser.find_element (By.ID, 'Last_name').get_attribute('class')
    assert 'success' in chrome_browser.find_element (By.ID, 'Address').get_attribute('class')
    assert 'success' in chrome_browser.find_element (By.ID, 'Email').get_attribute('class')
    assert 'success' in chrome_browser.find_element (By.ID, 'Phone').get_attribute('class')
    assert 'success' in chrome_browser.find_element (By.ID, 'City').get_attribute('class')
    assert 'success' in chrome_browser.find_element (By.ID, 'Country').get_attribute('class')
    assert 'success' in chrome_browser.find_element (By.ID, 'Job_position ').get_attribute('class')
    assert 'success' in chrome_browser.find_element (By.ID, 'Company').get_attribute('class')