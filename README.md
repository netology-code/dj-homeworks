

# Работа с менеджером урлов

Для запуска проекта необходимо:

## шаг первый

Установить зависимости:

```bash
pip install -r requirements.txt
```

## шаг второй

Cоздать файл с локальными настройками `file_server/settings_local.py`
и задать туда обязательные параметры:

* SECRET_KEY - секретная строка
* FILES_PATH - путь до директории с файлами

Например:

```python
import os

SECRET_KEY = 'd+mw&mscg5i&tx+#@bf+6m%e+d5z!u#!n%z-^o9u7y1felv2o&'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILES_PATH = os.path.join(BASE_DIR, 'files')
```

## шаг третий

Выполнить команду:

```bash
python manage.py runserver
```
