from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "The 'Add to basket' button is not present on the page"
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_btn.click()
        self.solve_quiz_and_get_code()

    def should_be_correct_product_name(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Book name is not present on the page"
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME_ADDED), "Book name is not present in the success message" 
        product_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        product_name_added = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ADDED).text
        assert product_name in product_name_added, "The product name in the information message doesn't match the name of the product added to the cart"

    def should_be_correct_product_price(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "Book price is not present on the page"
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_ADDED), "Book price is not present in the success message"
        product_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        product_price_added = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ADDED).text
        assert product_price in product_price_added, "The product price in the information message doesn't match the price of the product added to the cart"