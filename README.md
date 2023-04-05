## Проект
Смоук-тест для демонстрации решения.
1. Язык: [python](https://docs.python.org/3.10/index.html) v3.10,
2. Конфигурация тестов: [pytest](https://pytest.org/en/stable/contents.html) v7.2,
3. Фреймворк для тестирования веб-приложений: [Playwright](https://playwright.dev/python/docs/library) v1.31

## Тест-кейс
#### Проверка в поисковике google, калюкулятора на выполнение базовых математических операций.

### Предварительный шаги.
1. Открыть браузер.
2. Перейти на страницу google.com
3. Вести в поле поисковика "Калькулятор".
4. Нажать поиск и дождатся загрузки страницы с калькулятором.
### Шаги.
1. Вести в поле калькулятора арифметическое выражение.
### Ожидаемый результат.
Выведенный на экран результат совпадает со значение в переменной "".
### Постусловие.
Закрыть браузер.