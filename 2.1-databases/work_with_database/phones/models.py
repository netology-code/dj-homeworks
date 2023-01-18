from django.db import models

#from django.template.defaultfilters import slugify
#self.slug = slugify(self.name)

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    image_url = models.URLField(max_length=100)
    release_date = models.DateField()
    lte_exist = models.BooleanField()
    slug = models.SlugField(max_length=20)

    def __str__(self):
        return f'{self.slug}, {self.price}'

