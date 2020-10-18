from django.db import models
from autoslug import AutoSlugField


class Phone(models.Model):
    name = models.TextField(blank=True)
    price = models.IntegerField(null=True)
    image = models.TextField(blank=True)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name
