from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL_PART in self.driver.current_url, f"URL страницы не содержит '{LoginPageLocators.LOGIN_URL_PART}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина не найдена на странице"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации не найдена на странице"