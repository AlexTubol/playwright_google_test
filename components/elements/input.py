import allure
from playwright.sync_api import expect

from components.elements.base_element import Element


class Input(Element):
    @property
    def type_of(self) -> str:
        return 'input'

    def fill(self, value: str, validate_value=False, *args, **kwargs):
        with allure.step(f'Заполнить {self.type_of} "{self.name}" значением "{value}"'):
            locator = self.get_locator(*args, **kwargs)
            locator.fill(value)

            if validate_value:
                self.should_have_value(value, *args, **kwargs)

    def type(self, value: str, validate_value=False, *args, **kwargs):
        with allure.step(f'Ввести {self.type_of} "{self.name}" значение "{value}"'):
            locator = self.get_locator(*args, **kwargs)
            locator.type(value)

            if validate_value:
                self.should_have_value(value, *args, **kwargs)

    def press(self, value: str, *args, **kwargs):
        with allure.step(f'Симуляция нажатия кнопки "{value}"'):
            locator = self.get_locator(*args, **kwargs)
            locator.press(value)

    def should_have_value(self, value: str, *args, **kwargs):
        with allure.step(f'Проверить, что {self.type_of} "{self.name}" имеет значение "{value}"'):
            locator = self.get_locator(*args, **kwargs)
            expect(locator).to_have_value(value)

    def to_be_empty(self, *args, **kwargs):
        with allure.step(f'Проверить, что {self.type_of} "{self.name}" пустое"'):
            locator = self.get_locator(*args, **kwargs)
            expect(locator).to_be_empty()
