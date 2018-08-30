
# AB тестирование

## Задание




## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:

```bash
pip install -r requirements.txt
```

Создать файл с локальными настройками `app/settings_local.py`
и задать туда обязательные параметры:

* SECRET_KEY - секретная строка

Например:

```python
SECRET_KEY = 'd+mw&mscg5i&tx+#@bf+6m%e+d5z!u#!n%z-^o9u7y1felv2o&'
```

Выполнить команду:

```bash
python manage.py runserver
```