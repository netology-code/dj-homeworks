from django.db import models


class Phone(models.Model):
    brand = models.TextField(blank=True)
    model = models.TextField(blank=True)
    os = models.TextField(blank=True)
    cam = models.TextField(blank=True)
    color = models.TextField(blank=True)
    ram = models.TextField(blank=True)
    proc = models.TextField(blank=True)
    price = models.IntegerField(null=True)


class UniqPhone(models.Model):
    bt = models.TextField(default='-')
    wifi = models.TextField(default='-')
    sd = models.TextField(default='-')
    name = models.ForeignKey('Phone', null=True, on_delete=models.SET_NULL)
