from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Teg(models.Model):
    name = models.CharField(max_length=30)
    articles = models.ManyToManyField(Article, related_name='articles', through='ArticleTeg')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class ArticleTeg(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    teg = models.ForeignKey(Teg, on_delete=models.CASCADE, related_name='scopes')
    main_teg = models.BooleanField(verbose_name='Основной')