import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.window_size = (1920, 1080)
    browser.config.driver_name = "chrome"

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 6

    yield

    browser.quit()