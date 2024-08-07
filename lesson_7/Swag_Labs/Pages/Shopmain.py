from selenium.webdriver.common.by import By
from lesson_7.constants import Shop_URL

class ShopmainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(Shop_URL)

    def regisration_fieds(self):
        self._name = (By.ID, "user-name")
        self._pass = (By.ID, "password")
        self._log_button = (By.ID, "login-button")

        self.browser.find_element(*self._name).send_keys("standard_user")
        self.browser.find_element(*self._pass).send_keys("secret_sauce")
        self.browser.find_element(*self._log_button).click()

    def buy_issue(self):
        self.Sauce_Labs_Backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.Sauce_Labs_Bolt_Tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.Sauce_Labs_Onesie = (By.ID, "add-to-cart-sauce-labs-onesie")

    def click_issue(self):
        self.browser.find_element(*self.Sauce_Labs_Backpack).click()
        self.browser.find_element(*self.Sauce_Labs_Bolt_Tshirt).click()
        self.browser.find_element(*self.Sauce_Labs_Onesie).click()

    def info_container(self):
        self.Container = (By.ID,"shopping_cart_container")
        self.browser.find_element(*self.Container).click()

