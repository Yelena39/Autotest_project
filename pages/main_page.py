from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):

	def should_be_login_link(self):
	    """Checking if the main page has a link with login_link id."""
	    assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not present on the page"
	
	def go_to_login_page(self):
	    """Clicking the link with login_link id."""
	    login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
	    login_link.click()

	def should_be_login_url(self):
	    """Checking if the current page url has the "login" word in it."""
	    assert "login" in self.browser.current_url, "Login page link is incorrect"