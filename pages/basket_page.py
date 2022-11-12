from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

	def should_be_empty_basket(self):
		"""Checking for 4 seconds if the items form is absent from the page."""
		assert self.is_not_element_present(*BasketPageLocators.ITEMS_FORM), "There are items in the basket, but should not be"

	def should_be_empty_basket_message(self):
		"""Checking if 'basket is empty' message is present on the page."""
		assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "'Your basket is empty' message is not present, but should be"