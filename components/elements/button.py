import allure

from components.elements.base_element import Element


class Button(Element):
    @property
    def type_of(self) -> str:
        return 'button'

    def double_click(self, *args, **kwargs):
        with allure.step(f'Двойное нажатие {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(*args, **kwargs)
            locator.dblclick()
