import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

@pytest.mark.registered_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """Registering new user.

        opening browser ->
        going to the login page -> 
        generating email ->
        enerating password ->
        entering email and password into registration form and clicking "Register" ->
        checking if the new user is authorized

        """
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        """Checking for 4 seconds if success message is absent after the page is loaded."""
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """Checking the process of adding the product to cart.

        opening browser ->
        checking if success message is absent from the page -> 
        clicking "Add to basket" button ->
        checking if the product name in success message is correct ->
        checking if the product price in success message is correct

        """
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.should_be_success_message()
        page.should_be_correct_product_name()
        page.should_be_correct_product_price()


def test_guest_cant_see_success_message(browser):
    """Checking for 4 seconds if success message is absent after the page is loaded."""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.need_review
@pytest.mark.parametrize('link_end', [*range(7), 
                                     pytest.param(7, marks=pytest.mark.xfail(reason="Product name in success message is wrong")), 
                                     *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, link_end):
    """Checking the process of adding the product to cart.

    opening browser ->
    checking if success message is absent from the page -> 
    clicking "Add to basket" button ->
    checking if the product name in success message is correct ->
    checking if the product price in success message is correct

    """
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_end}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_success_message()
    page.should_be_correct_product_name()
    page.should_be_correct_product_price()

@pytest.mark.xfail(reason="Has to fail as success message should be present after adding to cart")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Checking for 4 seconds if success message is absent after adding to cart."""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Has to fail as has not been implemented yet")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Checking for 4 seconds if success message disappears after adding to cart."""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    """Checking if the page has login link present."""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Checking if it's possible to go to the login page.

    opening browser ->
    clicking the logink link -> 
    checking if the page opened is a login page

    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page.should_be_login_url()

@pytest.mark.new
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Checking if the basket is empty.

    opening browser ->
    checking if the product page has "View basket" button ->
    clicking the "View basket" button ->
    checking if current page url has "basket" word in it ->
    checking if the basket is empty ->
    checking if there is 'Your basket is empty' message on the page

    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_btn()
    page.go_to_basket_page()
    page.should_be_basket_url()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()