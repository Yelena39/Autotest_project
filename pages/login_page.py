from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_form(self):
        """Checking if the login page has the login_form id."""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        """Checking if the login page has the register_form id."""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not present"