from .pages.main_page import MainPage

def test_guest_should_see_login_link(browser):
    """Checking if the main page has login link."""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
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