import pytest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    def go_to_login_page(self, driver):
        login_link = driver.find_element(*self.LOGIN_LINK)
        login_link.click()
