from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'Модель телефона', max_length=64)
    price = models.IntegerField(u'Цена')
    image = models.ImageField(u'Изображение')
    slug = models.SlugField(u'URL', unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__())
        super(Phone, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "телефон"
        verbose_name_plural = "Телефон"
