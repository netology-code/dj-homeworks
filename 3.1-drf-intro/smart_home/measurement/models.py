from django.db import models


# TODO: опишите модель датчика (Sensor):
# - name — название датчика (CharField);
# - description — описание датчика, необязательное поле (CharField/TextField, blank=True).

# TODO: опишите модель измерения температуры (Measurement):
# - sensor — внешний ключ на датчик (ForeignKey, related_name='measurements');
# - temperature — температура при измерении (FloatField);
# - created_at — дата и время измерения (DateTimeField, auto_now_add=True).
