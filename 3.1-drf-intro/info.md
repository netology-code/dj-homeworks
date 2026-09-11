# Описание репозитория «Знакомство с API на примере Django REST framework»

Репозиторий содержит одну практическую работу по теме **«Компоненты Django REST Framework»**:
- `smart_home` — REST API «Умный дом» для датчиков температуры (создание эндпоинтов через DRF, сериализация моделей и обработка GET-запросов).

## Структура репозитория

```
3.1-drf-intro/
├── README.md                                  # Задание (информация, цели, критерии самопроверки)
├── info.md                                    # Этот файл (описание и инструкция)
├── checklist.md                               # Чек-лист самопроверки
│
└── smart_home/                                # Практическая работа «Умный дом»
    ├── README.md                              # Техническое задание по датчикам
    ├── manage.py                              # Управление проектом
    ├── requirements.txt                       # Зависимости (Django, DRF, psycopg2)
    ├── requests.http                          # Примеры API-запросов (GET)
    ├── measurement/                           # Приложение (датчики и измерения)
    │   ├── __init__.py
    │   ├── admin.py                           # Регистрация моделей в админке
    │   ├── apps.py
    │   ├── models.py                          # Модели Sensor и Measurement (нужно реализовать)
    │   ├── serializers.py                     # Сериализаторы (нужно реализовать)
    │   ├── views.py                           # Представления (нужно реализовать)
    │   ├── urls.py                            # Маршруты API (нужно реализовать)
    │   ├── tests.py
    │   ├── migrations/                        # Миграции
    │   │   └── __init__.py
    │   └── fixtures/
    │       └── sample_data.json               # Готовые данные для проверки GET-запросов
    └── smart_home/                            # Папка настроек проекта
        ├── __init__.py
        ├── settings.py                        # Настройки (DRF, приложение measurement)
        ├── urls.py                            # Подключение /api/
        ├── wsgi.py
        └── asgi.py
```

## Что за что отвечает

| Файл | Назначение | Что нужно сделать |
|------|------------|-------------------|
| `smart_home/measurement/models.py` | Модель датчика `Sensor` и измерения `Measurement` | Описать поля моделей |
| `smart_home/measurement/serializers.py` | `SensorSerializer` и `SensorDetailSerializer` | Настроить сериализацию (в т.ч. вложенные измерения) |
| `smart_home/measurement/views.py` | Представления `SensorListView` и `SensorDetailView` | Реализовать GET-список и GET-детально |
| `smart_home/measurement/urls.py` | Маршруты `/sensors/` и `/sensors/<id>/` | Зарегистрировать пути |
| `smart_home/measurement/fixtures/sample_data.json` | Примеры датчиков и измерений | Использовать для проверки (`loaddata`) |
| `smart_home/requests.http` | Примеры API-запросов | Проверить эндпоинты |
| `smart_home/smart_home/urls.py` | Подключение `measurement.urls` | Уже настроено |
| `smart_home/smart_home/settings.py` | Настройки проекта и подключение DRF | Уже настроено |

## Как открыть проект в IDE

### Вариант 1: PyCharm

1. Запустите PyCharm.
2. Нажмите **File → Open** и выберите папку `smart_home`.
3. Создайте виртуальное окружение.
4. Установите зависимости: `pip install -r requirements.txt`.

### Вариант 2: VS Code

1. Запустите VS Code.
2. Нажмите **File → Open Folder** и выберите папку `smart_home`.
3. Создайте виртуальное окружение: `python -m venv venv`.
4. Активируйте его (Linux/macOS: `source venv/bin/activate`, Windows: `venv\Scripts\activate.bat`).
5. Установите зависимости: `pip install -r requirements.txt`.

## Как запустить проект

Выполните из папки `smart_home`:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata sample_data
python manage.py runserver
```

> Примечание. Проект по умолчанию использует PostgreSQL (`netology_smart_home`). Если PostgreSQL не установлен, укажите в `smart_home/settings.py` другой движок, например SQLite.

Примеры проверки (откройте в браузере или Postman):
- **GET** `http://127.0.0.1:8000/api/sensors/` — список датчиков (ID, название, описание);
- **GET** `http://127.0.0.1:8000/api/sensors/1/` — информация по датчику со списком измерений температуры.
