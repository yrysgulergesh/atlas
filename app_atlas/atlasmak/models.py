
from django.db import models
from django.forms import ImageField
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from amplitude import Amplitude


from hitcount.models import HitCount
from hitcount.views import HitCountMixin

from hitcount.views import HitCountDetailView





# class Category(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.category = None

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('shop:product_list_by_category',
#                        args=[self.slug])


# class News(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Новости сайта')
#     content = models.TextField(blank=True, verbose_name='Текст')
#     created_at = models.DateField(auto_now_add=True, verbose_name='Добавить')
#     updated_at = models.DateField(auto_now=True, verbose_name='Обновить')
#     # delete_at = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Удалить')
#     photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
#     is_published = models.BooleanField(default=True)



    # def __str__(self):
    #     return self.title

    # class Meta:
    #     verbose_name = 'Новость'
    #     verbose_name_plural = 'Новости'


class Company(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name ='О компании'
        verbose_name_plural = 'О компании'
        ordering = ['title']



# class Certificate(models.Model):
#     photo = models.ImageField(upload_to = "atlasmak", null=True, blank=True)


#     class Meta:
#         verbose_name ='Сертификаты качества'
#         verbose_name_plural = 'Сертификаты качества'
#         ordering = ['photo']


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
        verbose_name_plural = 'Каталоги'
        ordering = ['title']



class Delivery(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name ='Доставка'
        verbose_name_plural = 'Доставки'
        ordering = ['title']

class Contact(models.Model):
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    created_on = models.DateField(auto_now_add=True)
    url = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Контакты'


# Всего посещений сайта
# class VisitNumber(models.Model):
#     count=models.IntegerField(verbose_name='Всего посещений сайта',default=0) # Всего посещений сайта
#     class Meta:
#         verbose_name = 'Всего посещений сайта'
#         verbose_name_plural = verbose_name
#     def __str__(self):
#         return str(self.count)

# Статистика посещений за один день
# class DayNumber(models.Model):
#     day=models.DateField(verbose_name='свидание',default=timezone.now)
#     count=models.IntegerField(verbose_name='Количество посещений сайта',default=0) # Всего посещений сайта
#     class Meta:
#         verbose_name = 'Статистика ежедневных посещений сайта'
#         verbose_name_plural = verbose_name
#     def __str__(self):
#         return str(self.day)
