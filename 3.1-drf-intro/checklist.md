# Чек-лист самопроверки

Отметьте галочками (✅) выполненные пункты. После прохождения чек-листа сравните своё решение с эталонным в приложении к заданию.

## Модели
- [ ] Модель `Sensor` содержит поле `name` (CharField)
- [ ] Модель `Sensor` содержит поле `description` (CharField или TextField, может быть пустым)
- [ ] Модель `Measurement` содержит поле `sensor` (ForeignKey на `Sensor`)
- [ ] Модель `Measurement` содержит поле `temperature` (FloatField)
- [ ] Модель `Measurement` содержит поле `created_at` (DateTimeField с `auto_now_add=True`)
- [ ] Применены миграции (`python manage.py makemigrations measurement` и `migrate`)

## Сериализаторы
- [ ] `SensorSerializer` выводит `id`, `name`, `description`
- [ ] `MeasurementSerializer` выводит `temperature` и `created_at`
- [ ] `SensorDetailSerializer` содержит вложенный список `measurements` (использован `MeasurementSerializer(read_only=True, many=True)`)
- [ ] `SensorDetailSerializer` выводит `id`, `name`, `description`, `measurements`

## Вьюхи и маршруты
- [ ] Для списка датчиков используется `ListAPIView`
- [ ] Для детального просмотра датчика используется `RetrieveAPIView`
- [ ] Указаны `queryset` и `serializer_class` в обоих представлениях
- [ ] В `urls.py` зарегистрированы маршруты `/sensors/` и `/sensors/<pk>/` на пространстве имён приложения
- [ ] Маршруты подключены к `smart_home/urls.py` через префикс `api/`

## Проверка работы
- [ ] Сервер запускается без ошибок (`python manage.py runserver`)
- [ ] Загружены тестовые данные (`python manage.py loaddata sample_data`)
- [ ] `GET /api/sensors/` возвращает список датчиков (id, name, description)
- [ ] `GET /api/sensors/1/` возвращает детальную информацию со списком измерений
- [ ] Ответы приходят в формате JSON

## Код и документация
- [ ] Код соответствует [стилю оформления](https://github.com/netology-code/codestyle/tree/master/python)
- [ ] Удалены `TODO`-комментарии
- [ ] Присутствуют служебные файлы проекта (`manage.py`, `requirements.txt`)
