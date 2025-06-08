import pytest
from pages.product_page import ProductPage

@pytest.mark.parametrize('promo', ["?promo=newYear"])
def test_guest_can_add_product_to_basket(driver, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/{promo}"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.should_be_product_added_to_basket()
    page.should_be_basket_total_equal_to_product_price()