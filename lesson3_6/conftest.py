import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

executable_path=r'D:\GoogleDrive\chromedriver.exe'

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language. For example: ru,es,fr")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    browser = None
    if user_language:
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError('--language not set')
    yield browser
    print("\nquit browser..")
    browser.quit()