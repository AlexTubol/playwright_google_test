from abc import ABC, abstractmethod

import allure
from playwright.sync_api import Locator, Page, expect


class Element(ABC):
    def __init__(self, page: Page, locator: str, name: str) -> None:
        self.page = page
        self.name = name
        self.locator = locator

    @property
    @abstractmethod
    def type_of(self) -> str:
        return 'element'

    def get_locator(self, *args, **kwargs) -> Locator:
        locator = self.locator.format(*args, **kwargs)
        return self.page.locator(locator)

    def click(self, *args, **kwargs) -> None:
        with allure.step(f'Кликнуть {self.type_of} по имени "{self.name}"'):
            locator = self.get_locator(*args, **kwargs)
            locator.click()

    def should_be_visible(self, *args, **kwargs):
        with allure.step(f'Проверить, что {self.type_of} "{self.name}" видны'):
            locator = self.get_locator(*args, **kwargs)
            expect(locator).to_be_visible()

    def should_contain_text(self, text: str, *args, **kwargs):
        with allure.step(f'Проверить, что {self.type_of} "{self.name}" имеет значение "{text}"'):
            locator = self.get_locator(*args, **kwargs)
            expect(locator).to_contain_text(text)
