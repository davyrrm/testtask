import os
import json
import pytest
from playwright.sync_api import sync_playwright

# Используем фикстуру для запуска и закрытия браузера для всех тестов
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) 
        yield browser
        browser.close()  

# Загрузка данных из JSON 
def load_json_data(test_num):
    with open(f'data/test_{test_num}.json', 'r') as file:
        return json.load(file)

# Тест кейсы с названиями
test_cases = [
    (1, 'base_case_zero'),
    (2, 'base_case_one'),
    (3, 'group_one_thousand'),
    (4, 'group_one_thousand_one'),
    (5, 'group_one_below_thousand'),
    (6, 'group_two_hundred_thousand'),
    (7, 'group_two_hundred_thousand_one'),
    (8, 'group_two_below_hundred_thousand'),
    (9, 'group_three_million'),
    (10, 'group_three_million_one'),
    (11, 'group_three_below_million'),
]

@pytest.mark.parametrize("test_num, test_name", test_cases, ids=[name for _, name in test_cases])
def test_impact_page(browser, test_num, test_name):
    page = browser.new_page()  # Инициализация страницы в браузере

    # Проверка существования папки output, создание если её нет
    if not os.path.exists('output'):
        os.makedirs('output')

    data = load_json_data(test_num)  # Загрузка тестовых данных
    # Перехват запроса с микрофронтенда и замена на json с тестовыми данными
    page.route('**/charity/ecoImpact/**', lambda route, request:
        route.fulfill(
            status=200,
            content_type='application/json',
            body=json.dumps(data)
        )
    )

    print(f"Running {test_name}")  

    # Переход на страницу с счетчиками
    page.goto('https://www.avito.ru/avito-care/eco-impact')

    # Поиск элемента и создание скриншота
    element = page.locator('.desktop-impact-items-F7T6E')
    element.screenshot(path=f'output/test_{test_num}.png')
    page.close()  # Закрытие страницы

