from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    img = models.FileField(upload_to='products/%Y/%m/%d/')

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.name) + ' ' + self.text[:50]
