from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
	BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
	BOOK_NAME_ADDED = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
	BOOK_PRICE_ADDED = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")