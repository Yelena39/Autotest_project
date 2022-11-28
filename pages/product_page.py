from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_cart(self):
        """Adding the product to cart.

        opening browser ->
        checking if the page has "Add to basket" button ->
        clicking "Add to basket" button ->
        solving math problem from alert and printing the code to console
        (the last step doesn't really relate to the test case itself, but needed in order to complete it)

        """
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "The 'Add to basket' button is not present on the page"
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_btn.click()
        self.solve_quiz_and_get_code()

    def should_be_correct_product_name(self):
        """Checking if the product name in success message is correct.

        checking if the page has the product name ->
        checking if the success message has the product name ->
        checking if the product name in success message matches the name of the product on the page

        """
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Book name is not present on the page"
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME_ADDED), "Book name is not present in the success message" 
        product_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        product_name_added = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ADDED).text
        assert product_name == product_name_added, "The product name in the information message doesn't match the name of the product added to the cart"

    def should_be_correct_product_price(self):
        """Checking if the product price in success message is correct.

        checking if the page has the product price ->
        checking if the success message has the product price ->
        checking if the product price in success message matches the price of the product on the page

        """
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "Book price is not present on the page"
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_ADDED), "Book price is not present in the success message"
        product_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        product_price_added = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ADDED).text
        assert product_price == product_price_added, "The product price in the information message doesn't match the price of the product added to the cart"

    def should_be_success_message(self):
        """Checking if success message is present on the page."""
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not present, but should be"

    def should_disappear_success_message(self):
        """Checking for 4 seconds if success message disappears from the page."""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message has not disappeared in 4 sec, but should have"

    def should_not_be_success_message(self):
        """Checking for 4 seconds if success message is absent from the page."""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is present, but should not be"