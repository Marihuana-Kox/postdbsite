from django.db import models


class Category(models.Model):
    '''Категории для статей и страниц'''
    name = models.CharField('Название категории', max_length=150)
    description = models.CharField('Описание категории', max_length=250)
    image = models.ImageField(
        'Изображение', upload_to='category/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class PageArticles(models.Model):
    '''Статьи и страницы'''
    name = models.CharField('Название страницы',
                            max_length=150, default=0)
    title = models.CharField('Заголовок статьи', max_length=200)
    description = models.CharField('Длинный заголовок', max_length=250)
    article = models.TextField('Текст статьи')
    image = models.ImageField(
        'Изображение', upload_to='pages/', blank=True, null=True)
    pub_date = models.DateField('Дата публикации', auto_now=True)
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.title

    class Meta:
        ordering = ["-name"]
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
