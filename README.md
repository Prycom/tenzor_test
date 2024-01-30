# tenzor_test
В данном репозитории реализовано тестовое задание. В реализации были использованы `pytest`, `selenium`, `allure`.

## Установка
Для работы потребуется:
- python
- chrome или chromium
- chromedriver

Для установки необходимых зависимостей, создайте виртуальное окружение
`python3 -m venv .venv`

Далее активируйте окружение:
- `source ./.venv/bin/activate` в Linux
- `./.venv/Scripts/activate` в Windows

И установите зависимости `pip install -r requirements.txt`

Также установите [allure](https://github.com/allure-framework) в вашу систему

## Конфигурация
В файле `config.py`, в переменную `DOWNLOAD_PATH` вставьте путь скачивания файлов

## Запуск
Для запуска тестов используйте команду:
- `pytest -sv tests/test.py --alluredir=reports`


Для запуска allure используйте команду:
- `allure serve reports/`

## P.S.
Решение написано и протестировано `Chromium 121.0.6167.85 built on Debian 12.4, running on Debian 12.4`
