from selenium.common.exceptions import NoAlertPresentException
import math
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_product_added_to_basket(self):
        product_name = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.driver.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == message_product_name, "Product name in message doesn't match"

    def should_be_basket_total_equal_to_product_price(self):
        product_price = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.driver.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, "Basket total doesn't match product price"