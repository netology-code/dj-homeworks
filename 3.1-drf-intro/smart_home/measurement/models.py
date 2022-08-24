from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название датчика')
    image = models.ImageField(upload_to='sensor_images/%Y%m%d/', null=True, verbose_name='Внешний вид')
    description = models.CharField(max_length=200, verbose_name='Описание датчика')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['id']

    def __str__(self):
        return self.title


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура при измерении')
    measurement_date = models.DateTimeField(auto_now=True, verbose_name='Дата измерения')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['measurement_date']

    def __str__(self):
        return f'Дата измерения: {self.measurement_date}, Температура: {self.temperature}'
