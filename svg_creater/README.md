# SVG CREATER
Данный скрипт позволяет создавать SVG-файлы. Создание SVG-файлов осуществляется с помощью библиотеки [svgwrite](https://pypi.org/project/svgwrite/1.4.3/).

## Как запустить скрипт

Для начала необходимо развернуть виртуальную среду с помощью команды:

```bash
python -m venv venv
```

Загрузить все необходимые библиотеки:

```bash
pip install -r requirements.txt
```

Далее запустить скрипт:

```bash
python app.py
```

## Структура проекта

* `src`: Папка с исходными SVG-файлами.
* `venv`: Виртуальная среда.
* `requirements.txt`: Файл с необходимыми библиотеками.
* `index.html`: Страница с SVG-файлам.
* `app.py`: Приложение для создания SVG-файлов.

```bash
svg_creater
    ├── src
    │   └── salavat.svg
    ├── requirements.txt
    ├── index.html
    └── app.py
```

## Пример генерации изображения

![created_svg](src/salavat.svg)
