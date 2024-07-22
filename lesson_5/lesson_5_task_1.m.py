from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()
    
firefox.get ('http://the-internet.herokuapp.com/add_remove_elements/')
for i in range(5):   
    add_Button = firefox.find_element (By.XPATH, ("//button[text()='Add Element']")).click() 
sleep(1)    
firefox_delete_buttons =firefox.find_elements("xpath",'//button[text()="Delete"]')
print( f"размер списка кнопок Delete: {len(firefox_delete_buttons)}")
firefox.quit()    
         