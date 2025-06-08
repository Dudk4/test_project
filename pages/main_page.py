import pytest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        self.driver.find_element(*MainPageLocators.LOGIN_LINK).click()
        return LoginPage(self.driver, self.driver.current_url)  # Переход на новую страницу

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

