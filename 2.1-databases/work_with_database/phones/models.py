from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    #id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    #slug = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    release_date = models.CharField(max_length=50)
    lte_exists = models.CharField(max_length=20)
    #

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
