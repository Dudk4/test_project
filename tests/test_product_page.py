import pytest
from pages.product_page import ProductPage
from conftest import driver

@pytest.mark.parametrize('promo', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3",
    "?promo=offer4", "?promo=offer5", "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(driver, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/{promo}"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.should_be_product_added_to_basket()
    page.should_be_basket_total_equal_to_product_price()


def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(driver, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()

