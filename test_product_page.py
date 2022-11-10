from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    """Checking the process of adding the product to cart.

    opening browser -> 
    clicking "Add to basket" button ->
    checking if the product name in success message is correct ->
    checking if the product price in success message is correct

    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_correct_product_name()
    page.should_be_correct_product_price()