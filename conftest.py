import pytest
from playwright.sync_api import Playwright, Page

from data_generation import generating_test_data
from page.models.calculator_search_page import CalculatorSearchPage
from page.models.main_page import MainPage
from resources import SEARCH_TEXT


@pytest.fixture(scope='function')
def before_each_calculator_search_page(main_page):
    main_page.go_to_page()
    main_page.search_text(SEARCH_TEXT)
    yield


@pytest.fixture(scope="session", autouse=True)
def page(playwright: Playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    yield page
    browser.close()


@pytest.fixture(scope='function', params=generating_test_data())
def test_data(request):
    return request.param


@pytest.fixture(scope="function")
def main_page(page: Page) -> MainPage:
    return MainPage(page)


@pytest.fixture(scope="function")
def calculator_search_page(page: Page) -> CalculatorSearchPage:
    return CalculatorSearchPage(page)
