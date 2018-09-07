from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Article(models.Model):
    title = models.CharField(u'Заголовок', max_length=32)
    content = models.TextField(u'Содержимое', max_length=20000)
    pay = models.BooleanField(u'Платный контент')

    def __str__(self):
        return self.title
