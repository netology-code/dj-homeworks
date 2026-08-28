# Описание репозитория «Работа с ORM»

## Структура репозитория

```
2.1-databases/
├── README.md                              # Главный README с описанием всех заданий
├── info.md                                # Этот файл — описание структуры
├── work_with_database/                    # ОБЯЗАТЕЛЬНОЕ задание
│   ├── README.md                          # Описание задания
│   ├── manage.py                          # Управление проектом
│   ├── requirements.txt                   # Зависимости
│   ├── phones.csv                         # Данные для импорта
│   ├── phones/                            # Приложение phones
│   │   ├── __init__.py
│   │   ├── admin.py                       # Настройки админки
│   │   ├── apps.py                        # Конфигурация приложения
│   │   ├── models.py                      # Модели — ЗДЕСЬ НУЖНО ПРАВИТЬ
│   │   ├── tests.py                       # Тесты
│   │   ├── views.py                       # View-функции — ЗДЕСЬ НУЖНО ПРАВИТЬ
│   │   └── management/                    # Кастомные команды
│   │       └── commands/
│   │           └── import_phones.py       # Скрипт импорта — ЗДЕСЬ НУЖНО ПРАВИТЬ
│   ├── templates/                         # Шаблоны
│   │   ├── base.html
│   │   ├── catalog.html
│   │   └── product.html
│   └── main/                              # Настройки проекта
│       ├── __init__.py
│       ├── settings.py
│       ├── urls.py                        # Маршруты — ЗДЕСЬ НУЖНО ПРАВИТЬ
│       └── wsgi.py
├── models_list_displaying/                # ДОПОЛНИТЕЛЬНОЕ задание
│   ├── README.md                          # Описание задания
│   ├── manage.py
│   ├── requirements.txt
│   ├── books/                             # Приложение books
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                      # Модели — ЗДЕСЬ НУЖНО ПРАВИТЬ
│   │   ├── views.py                       # View-функции — ЗДЕСЬ НУЖНО ПРАВИТЬ
│   │   ├── converters.py                  # Конвертер для даты
│   │   └── migrations/                    # Миграции
│   ├── fixtures/                          # Начальные данные
│   │   └── books.json
│   ├── templates/
│   │   ├── base.html
│   │   └── books/
│   │       └── books_list.html
│   └── main/
│       ├── settings.py
│       └── urls.py                        # Маршруты — ЗДЕСЬ НУЖНО ПРАВИТЬ
└── res/                                   # Ресурсы (скриншоты)
```

## Что за что отвечает

### Обязательное задание (work_with_database)

| Файл | Назначение | Что нужно сделать |
|------|------------|-------------------|
| `phones/models.py` | Модель данных | Создать модель `Phone` со всеми полями |
| `phones/views.py` | View-функции | Реализовать `show_catalog` и `show_product` |
| `phones/management/commands/import_phones.py` | Импорт данных | Написать скрипт для загрузки из CSV |
| `main/urls.py` | Маршруты | Настроить маршруты для каталога и страницы телефона |

### Дополнительное задание (models_list_displaying)

| Файл | Назначение | Что нужно сделать |
|------|------------|-------------------|
| `books/models.py` | Модель данных | Создать модель `Book` |
| `books/views.py` | View-функции | Реализовать `books_view` с обработкой даты |
| `main/urls.py` | Маршруты | Настроить маршруты с конвертером даты |

## Как работать с репозиторием

### 1. Клонируйте репозиторий

```bash
git clone <ссылка на репозиторий>
cd 2.1-databases
```

### 2. Выберите задание

Перейдите в папку нужного задания:

```bash
# Для обязательного задания
cd work_with_database

# Для дополнительного задания
cd models_list_displaying
```

### 3. Создайте виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 4. Установите зависимости

```bash
pip install -r requirements.txt
```

### 5. Выполните миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Загрузите данные (для обязательного задания)

```bash
python manage.py import_phones
```

### 7. Запустите сервер

```bash
python manage.py runserver
```

### 8. Проверьте результат

Откройте в браузере:
- `http://127.0.0.1:8000/catalog/` — каталог телефонов
- `http://127.0.0.1:8000/books/` — библиотека

## Как отправить работу

1. Внесите изменения в требуемые файлы.
2. Сохраните все изменения.
3. Создайте коммит:
   ```bash
   git add .
   git commit -m "Решение задания по ORM"
   git push
   ```
