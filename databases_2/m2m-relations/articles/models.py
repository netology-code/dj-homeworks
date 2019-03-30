from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):

    topic = models.CharField(max_length=256, verbose_name='Название')
    articles = models.ManyToManyField(Article, through='ArticleScope')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.topic

    @property
    def is_main(self):
        return 



class ArticleScope(models.Model):

    is_main = models.BooleanField(verbose_name='Основной')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='Статья')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'

    def __str__(self):
        return f'{self.article}-{self.scope}'

    @property
    def topic(self):
        return self.scope.topic
