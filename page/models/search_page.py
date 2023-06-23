from playwright.sync_api import expect, Page

from page.models.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_BOX = "Найти"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @property
    def type_page(self) -> str:
        return 'search page'
