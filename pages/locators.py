from selenium.webdriver.common.by import By

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini [href*='basket']")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
	REGISTER_FORM_PASS = (By.CSS_SELECTOR, "[name='registration-password1']")
	REGISTER_FORM_PASS_CONFIRM = (By.CSS_SELECTOR, "[name='registration-password2']")

class ProductPageLocators():
	ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
	BOOK_NAME_ADDED = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
	BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
	BOOK_PRICE_ADDED = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasketPageLocators():
	ITEMS_FORM = (By.CSS_SELECTOR, "#basket_formset")
	BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")