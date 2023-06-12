import pytest
from playwright.sync_api import Playwright

from PageObject.models.main_page import MainPage
from data_generation import generating_test_data
from resources import SEARCH_TEXT, GOOGLE_URL, GOOGLE_TITLE


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page):
    page = MainPage(page)
    page.go_to_google(GOOGLE_URL, GOOGLE_TITLE)
    page.search_text(SEARCH_TEXT)
    yield


@pytest.fixture(scope="session", autouse=True)
def page(playwright: Playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    yield page
    browser.close()


@pytest.fixture(scope='class', params=generating_test_data())
def test_data(request):
    return request.param
