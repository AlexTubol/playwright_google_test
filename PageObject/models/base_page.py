"""Абстракция страницы."""


class BasePage:

    def __init__(self, page):
        self.page = page

    def go_to_page(self, url):
        return self.page.goto(url)

    def find_element(self, locator):
        return self.page.locator(locator)
