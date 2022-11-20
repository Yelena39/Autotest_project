from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
	"""Returns the BasePage object with the delegated arguments.
	
	:param args:
    :param kwargs:

    """
	def __init__(self, *args, **kwargs):
		super(MainPage, self).__init__(*args, **kwargs)