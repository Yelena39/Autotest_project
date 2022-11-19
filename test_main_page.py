import pytest
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_should_see_login_link(self, browser):
        """Checking if the main page has login link."""
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        """Checking going to login page.

        opening browser -> 
        clicking the login link ->
        checking if current page url has "login" word in it

        """
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()   
        page.go_to_login_page()
        page.should_be_login_url()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """Checking if the basket is empty.

    opening browser ->
    checking if the main page has "View basket" button ->
    clicking the "View basket" button ->
    checking if current page url has "basket" word in it ->
    checking if the basket is empty ->
    checking if there is 'Your basket is empty' message on the page

    """
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_btn()
    page.go_to_basket_page()
    page.should_be_basket_url()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()