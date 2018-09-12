from django.db import models


class Article(models.Model):
    """
        Модель Статьи
    """
    title = models.CharField("Название", max_length=64)
    text = models.TextField("Текст")
    sections = models.ManyToManyField("Section", through="SectionMember", related_name="articles")
    pub_date = models.DateField("Дата публикации")
    image = models.ImageField("Изображение", upload_to="article_image", blank=True)

    def __str__(self):
        return self.title


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
