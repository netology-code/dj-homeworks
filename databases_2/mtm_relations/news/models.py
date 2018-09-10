from django.db import models


class Article(models.Model):
    title = models.CharField("Название", max_length=64)
    text = models.TextField("Текст")
    sections = models.ManyToManyField("Section", through="SectionMember", related_name="articles")
    pub_date = models.DateField("Дата публикации")
    image = models.ImageField("Изображение", upload_to="article_image", blank=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    name = models.CharField("Название", max_length=64)

    def __str__(self):
        return self.name


class SectionMember(models.Model):
    article = models.ForeignKey("Article", on_delete=models.DO_NOTHING, related_name="topics")
    section = models.ForeignKey("Section", on_delete=models.DO_NOTHING, related_name="topics")
    main = models.BooleanField(default=False)

    def __str__(self):
        return "{0} - {1}".format(self.section.name, self.article.title)