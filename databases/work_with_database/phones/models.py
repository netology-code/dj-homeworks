from django.db import models
from django.utils.text import slugify


class Phone(models.Model):

    id = models.IntegerField(
        primary_key=True,
    )
    name = models.CharField(
        verbose_name='название модели',
        max_length=255,
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=7,
        decimal_places=2
    )
    image = models.CharField(
        verbose_name='URL изображения',
        max_length=255,
    )
    release_date = models.DateField(
        verbose_name='дата релиза'
    )
    lte_exists = models.BooleanField(
        verbose_name='имеется LTE'
    )
    slug = models.CharField(
        verbose_name='слагифицированное имя',
        max_length=255,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
