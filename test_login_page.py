from .pages.login_page import LoginPage

def test_guest_should_see_login_form(browser):
	"""Checking if the login page has the login form."""
	link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
	page = LoginPage(browser, link)
	page.open()
	page.should_be_login_form()

def test_guest_should_see_register_form(browser):
	"""Checking if the login page has the registration form."""
	link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
	page = LoginPage(browser, link)
	page.open()
	page.should_be_register_form()