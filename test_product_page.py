import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('link_end', [*range(7), 
                                     pytest.param(7, marks=pytest.mark.xfail(reason="Product name in success message is wrong")), 
                                     *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, link_end):
    """Checking the process of adding the product to cart.

    opening browser -> 
    clicking "Add to basket" button ->
    checking if the product name in success message is correct ->
    checking if the product price in success message is correct

    """
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_end}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_correct_product_name()
    page.should_be_correct_product_price()