import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: any language is accepted')
    parser.addoption('--headless', action='store', default='false',
                     help='Open a browser invisible, without GUI is used by default')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    headless = request.config.getoption('headless')

    firefox_options = FirefoxOptions()
    firefox_options.set_preference('intl.accept_languages', language)

    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})

    if browser_name == 'firefox' and headless == 'true':
        firefox_options.add_argument('--headless')
        firefox_options.add_argument('--width=1920')
        firefox_options.add_argument('--height=1080')
        print('\nstart firefox browser for test..')
        browser = webdriver.Firefox(options=firefox_options)

    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        browser = webdriver.Firefox(options=firefox_options)

    elif headless == 'true':
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=chrome_options)

    else:
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=chrome_options)

    yield browser
    print("\nquit browser..")
    browser.quit()