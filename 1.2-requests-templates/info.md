# Описание репозитория «Обработка запросов и шаблоны»

Репозиторий содержит две практические работы по теме **«Обработка HTTP-запросов и передача данных в шаблон»**:
- `recipes` — сервис-помощник для приготовления блюд (обработка GET-параметров и передача контекста в шаблон);
- `pagination` — реализация пагинации по CSV-файлу (использование Django Paginator).

## Структура репозитория

```
1.2-requests-templates/
├── README.md                              # Описание обеих практических работ
├── info.md                                # Этот файл (описание и инструкция)
│
├── recipes/                               # Практическая работа «Рецепты»
│   ├── README.md                          # Задание по рецептам
│   ├── manage.py                          # Управление проектом
│   ├── requirements.txt                   # Зависимости
│   ├── calculator/                        # Приложение (расчёт ингредиентов)
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── views.py                       # DATA с рецептами + view (нужно реализовать)
│   │   ├── migrations/                    # Миграции
│   │   └── templates/calculator/
│   │       └── index.html                 # Шаблон для вывода рецепта
│   └── recipes/                           # Папка настроек проекта
│       ├── __init__.py
│       ├── settings.py
│       ├── urls.py
│       ├── wsgi.py
│       └── asgi.py
│
└── pagination/                            # Практическая работа «Пагинация»
    ├── README.md                          # Задание по пагинации
    ├── manage.py                          # Управление проектом
    ├── requirements.txt                   # Зависимости
    ├── data-398-2018-08-30.csv            # Данные об остановках транспорта
    ├── assets/css/                        # Стили (skeleton/normalize)
    │   ├── normalize.css
    │   └── skeleton.css
    ├── res/result.png                     # Пример ожидаемого результата
    ├── stations/                          # Приложение (отображение остановок)
    │   ├── __init__.py
    │   ├── views.py                       # bus_stations (нужно реализовать)
    │   ├── urls.py
    │   └── templates/stations/
    │       └── index.html                 # Шаблон вывода остановок
    └── pagination/                        # Папка настроек проекта
        ├── __init__.py
        ├── settings.py                    # BUS_STATION_CSV (путь к csv-файлу)
        ├── urls.py
        ├── wsgi.py
        └── asgi.py
```

## Что за что отвечает

| Файл | Назначение | Что нужно сделать |
|------|------------|-------------------|
| `recipes/calculator/views.py` | Данные рецептов + view | Реализовать отображение рецепта и учёт параметра `servings` |
| `recipes/calculator/templates/calculator/index.html` | Шаблон рецепта | Сверстать вывод ингредиентов |
| `pagination/stations/views.py` | View `bus_stations` | Реализовать чтение CSV и пагинацию |
| `pagination/stations/templates/stations/index.html` | Шаблон остановок | Сверстать вывод страницы с постраничным переходом |
| `pagination/pagination/settings.py` | Настройки | Указать `BUS_STATION_CSV` |

## Как открыть проект в IDE

### Вариант 1: PyCharm

1. Запустите PyCharm.
2. Нажмите **File → Open** и выберите папку нужной практической работы (`recipes` или `pagination`).
3. Создайте виртуальное окружение.
4. Установите зависимости: `pip install -r requirements.txt`.

### Вариант 2: VS Code

1. Запустите VS Code.
2. Нажмите **File → Open Folder** и выберите папку нужной практической работы.
3. Создайте виртуальное окружение: `python -m venv venv`.
4. Активируйте его (Linux/macOS: `source venv/bin/activate`, Windows: `venv\Scripts\activate.bat`).
5. Установите зависимости: `pip install -r requirements.txt`.

## Как запустить проект

Для каждой практической работы (`recipes` и `pagination`) выполните из её папки:

```bash
pip install -r requirements.txt
python manage.py runserver
```

Примеры проверки:
- **Рецепты:** откройте `http://127.0.0.1:8000/omlet/` — список ингредиентов на 1 порцию; добавьте `?servings=4` — на 4 порции.
- **Пагинация:** откройте `http://127.0.0.1:8000/` — список остановок с постраничным выводом.
