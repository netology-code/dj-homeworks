# Описание репозитория «Тестирование Django-приложений с использованием Pytest»

## Структура репозитория

```
3.4-django-testing/
├── README.md                              # Главный README
├── info.md                                # Этот файл
└── django_testing/                        # Папка с проектом
    ├── README.md                          # Описание задания
    ├── manage.py                          # Управление проектом
    ├── requirements.txt                   # Основные зависимости
    ├── requirements-dev.txt               # Зависимости для разработки (включая pytest)
    ├── pytest.ini                         # Настройка Pytest
    ├── django_testing/                    # Настройки проекта
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    ├── students/                          # Приложение
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py                      # Модели (Student, Course)
    │   ├── views.py                       # ViewSet
    │   ├── serializers.py                 # Сериализаторы
    │   ├── filters.py                     # Фильтры
    │   └── migrations/                    # Миграции
    └── tests/                             # ТЕСТЫ (нужно создать)
        ├── __init__.py
        ├── conftest.py                    # Фикстуры
        └── students/
            ├── __init__.py
            └── test_courses_api.py        # Тесты для API
```

## Что за что отвечает

| Файл | Назначение | Что нужно сделать |
|------|------------|-------------------|
| `tests/conftest.py` | Фикстуры | Создать фикстуры для API и фабрик |
| `tests/students/test_courses_api.py` | Тесты API | Написать все тесты для CRUD-операций |
| `students/models.py` | Модели | Добавить валидацию (доп. задание) |

## Как открыть проект в IDE

### Вариант 1: PyCharm

1. Запустите PyCharm
2. Нажмите **File → Open** и выберите папку `django_testing`
3. Создайте виртуальное окружение
4. Установите зависимости: `pip install -r requirements-dev.txt`

### Вариант 2: VS Code

1. Запустите VS Code
2. Нажмите **File → Open Folder** и выберите папку `django_testing`
3. Создайте виртуальное окружение: `python -m venv venv`
4. Активируйте его и установите зависимости

## Как запустить тесты

```bash
# Установка зависимостей
pip install -r requirements-dev.txt

# Выполнение миграций
python manage.py migrate

# Запуск тестов
pytest -v

# Запуск с проверкой покрытия
pytest --cov=students --cov-report=term
```

## Как измерить покрытие кода

```bash
pytest --cov=students --cov-report=html
```

После этого откройте `htmlcov/index.html` в браузере.
