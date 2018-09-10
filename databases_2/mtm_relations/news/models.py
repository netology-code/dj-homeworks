from django.db import models


class Article(models.Model):
    """
        Модель Статьи
    """
    pass


class Section(models.Model):
    """
        Модель Раздела
    """
    pass


class SectionMember(models.Model):
    """
        Модель для связи Статьи и Раздела
    """
    pass
