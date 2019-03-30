from django.db import models

# Create your models here.

class Processor(models.Model):

    processor_model = models.CharField(
        verbose_name='название модели',
        max_length=255,
    )
    processor_frequency = models.PositiveIntegerField(
        verbose_name='тактовая частота',
        null=True,
        blank=True,
    )
    processor_cores = models.PositiveIntegerField(
        verbose_name='количество ядер',
    )

    def __str__(self):
        return f'{self.processor_model}, {str(self.processor_frequency) + " МГц, " if self.processor_frequency else ""}{self.processor_cores} ядер'


class ScreeenResolution(models.Model):

    vertical_screen_resolution = models.PositiveIntegerField(
        verbose_name='разрешение по-вертикали',
    )
    horisontal_screen_resolution = models.PositiveIntegerField(
        verbose_name='разрешение по-горизонтали',
    )

    def __str__(self):
        return f'{self.vertical_screen_resolution}×{self.horisontal_screen_resolution}'


class DeviceOS(models.Model):

    device_os_family= models.CharField(
        verbose_name='семейство',
        max_length=255,
    )
    device_os_name = models.CharField(
        verbose_name='название системы',
        max_length=255,
    )

    def __str__(self):
        return f'{self.device_os_family} {self.device_os_name}'


class Manufacturer(models.Model):

    manufacturer_name = models.CharField(
        verbose_name='имя',
        max_length=255,
    )

    def __str__(self):
        return self.manufacturer_name


class Camera(models.Model):

    camera_type = models.CharField(
        verbose_name='тип',
        max_length=255,
    )
    camera_matrix = models.PositiveIntegerField(
        verbose_name='матрица'
    )

    def __str__(self):
        return f'{self.camera_type} {self.camera_matrix} МП'


class Phone(models.Model):

    phone_model = models.CharField(
        verbose_name='название модели',
        max_length=255,
    )
    phone_price = models.DecimalField(
        verbose_name='цена',
        max_digits=7,
        decimal_places=2
    )
    phone_os = models.ForeignKey(
        DeviceOS,
        models.PROTECT,
        verbose_name='операционная система'
    )
    phone_manufacturer = models.ForeignKey(
        Manufacturer,
        models.PROTECT,
        verbose_name='производитель'
    )
    phone_memory = models.FloatField(
        verbose_name='размер оперативной памяти',
    )
    phone_ppi = models.PositiveIntegerField(
        verbose_name='число пикселей на дюйм',
        null=True,
        blank=True,
    )
    phone_cameras = models.ManyToManyField(
        Camera,
        verbose_name='камера'
    )
    phone_processor = models.ForeignKey(
        Processor,
        models.PROTECT,
        verbose_name='процессор'
    )
    phone_screen_resolution = models.ForeignKey(
        ScreeenResolution,
        models.PROTECT,
        verbose_name='разрешение экрана'        
    )
    phone_fm_radio = models.BooleanField(
        verbose_name='FM-радио',
    )
    phone_addition = models.TextField(
        verbose_name='дополнительные параметры',
        blank=True,
        max_length=4096
    )

    def __str__(self):
        return self.phone_model


