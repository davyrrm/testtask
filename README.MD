## Инструкция к получению скриншотов счётчиков

### 1. Клонирование репозитория
Для начала вам нужно клонировать данный репозиторий с GitHub. Откройте командную строку и введите следующие команды:

```shell
git clone https://github.com/davyrrm/testtask
```

### 2. Установка Python
Если у вас ещё не установлен Python, скачайте его с [официального сайта Python](https://www.python.org/downloads/) и следуйте инструкциям по установке для вашей операционной системы.

### 3. Установка библиотек
Вам потребуются библиотеки pytest и playwright для запуска скрипта. Установите их, используя pip, стандартный пакетный менеджер для Python. В командной строке выполните следующие команды:

```shell
pip install pytest
pip install playwright
```

### 4. Запуск тестов

Перед запуском тестов, в командной строке введите cd и перейдите в папку проекта.

Для запуска тестов вы можете использовать команду pytest с различными опциями в зависимости от ваших потребностей:

Стандартный запуск в headless режиме (браузер не отображается):
```shell
pytest eco_counters_test.py
```
Запуск в режиме с видимым браузером (headed mode), чтобы видеть, что происходит во время тестов:
```shell
pytest --headed eco_counters_test.py
```

Запуск тестов в определенном браузере, например, в Chrome (для этого браузера используется engine Chromium):
```shell
pytest --browser chromium eco_counters_test.py
```
Если вам нужно быстро протестировать изменения без визуального контроля, используйте стандартный запуск.
Если вы хотите видеть, как тесты выполняются в реальном времени, выбирайте запуск в headed режиме.
Если вы тестируете функционал, который может специфически работать в разных браузерах, или если у вас есть требования к определенному браузеру, используйте опцию --browser.

### 5. Просмотр результатов
После завершения тестов результаты (скриншоты экосчётчиков) будут сохранены в папке `output`. Проверьте папку, чтобы увидеть результаты ваших тестов.

### 6. Что делать при возникновении ошибок
Если тесты не запускаются или вы получаете ошибки, убедитесь, что вы правильно установили все зависимости и ваш тестовый сценарий соответствует текущему состоянию веб-страницы, которую вы тестируете. Обратитесь к [документации pytest](https://docs.pytest.org/en/7.1.x/contents.html/) и [playwrite](https://playwright.dev/docs/intro) за более подробной информацией о возможных ошибках и способах их решения.
