"""Абстракция страницы."""
import allure
from abc import ABC, abstractmethod
from playwright.sync_api import Page, Response, expect


class BasePage(ABC):
    def __init__(self, page: Page):
        self.page = page

    @property
    @abstractmethod
    def name_page(self) -> str:
        return 'page'

    def go_to(self, url: str) -> Response:
        with allure.step(f'Открывает страницу "{url}"'):
            return self.page.goto(url)

    def should_have_title(self, value: str):
        with allure.step(f'Проверить, что title имеет значение {value}'):
            expect(self.page).to_have_title(value)
