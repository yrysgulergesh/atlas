from django.db import models
from django.forms import ImageField


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Новости сайта')
    content = models.TextField(blank=True, verbose_name='Текст')
    created_at = models.DateField(auto_now_add=True, verbose_name='Добавить')
    updated_at = models.DateField(auto_now=True, verbose_name='Обновить')
    # delete_at = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Удалить')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Company(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name ='О компании'
        ordering = ['title']



class Certificate(models.Model):
    photo = models.ImageField(upload_to = "atlasmak", null=True, blank=True)


class Meta:
        verbose_name ='Сертификаты качества'
        ordering = ['photo']


class Catalog(models.Model):
    image = models.ImageField(upload_to = "atlasmak", null=True, blank=True)
    number = models.CharField(max_length=20)
    title = models.CharField(max_length=225)
    description = models.TextField()
    specifications = models.CharField(max_length=225)
    price = models.CharField(max_length=225)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name ='Каталог'
        ordering = ['title']



class Delivery(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name ='Доставка'
        ordering = ['title']