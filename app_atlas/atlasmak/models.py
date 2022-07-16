# from enum import Enum, Flag
from unicodedata import name
from amplitude import Amplitude
from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField, ImageField
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from hitcount.models import HitCount
from hitcount.views import HitCountDetailView, HitCountMixin

# class PostCountHitDetailView(HitCountDetailView):
#         # your model goes here
#     count_hit = True    # set to True if you want it to try and count the hit


# class Category(models.Model):
#     title = models.CharField(max_length=200, db_index=True)
#     # parameters = models.ForeignKey(
#     #     on_delete=models.CASCADE,
#     #     null=True,
#     #     blank=True)
#     class Meta:
#         # ordering = ('name',)
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'

# def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     self.category = None

# def __str__(self):
#     return self.title

# def get_absolute_url(self):
#     return reverse('shop:product_list_by_category',
#                    args=[self.parameters])


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


# # class Category(models.Model):
# #     # id = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=50)
# #     parent = models.ForeignKey(on_delete=models.CASCADE, null=True,  blank=True)


#     class Meta:
#         verbose_name = "Категория"
#         verbose_name_plural = "Категории"


#     def __str__(self):
#         return f"{self.name} ({self.parent})"

class Company(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "О компании"
        verbose_name_plural = "О компании"
        ordering = ["title"]


# class Certificate(models.Model):
#     photo = models.ImageField(upload_to = "atlasmak", null=True, blank=True)


#     class Meta:
#         verbose_name ='Сертификаты качества'
#         verbose_name_plural = 'Сертификаты качества'
#         ordering = ['photo']


class Catalog(models.Model):


    PARAMETER_CHOICES = [
        ("1", "Стандартное напряжение"),
        ("2", "Частота"),
        ("3", "Суммарная мощность"),
        ("4", "Давление воздуха"),
        ("5", "Потребление воздуха"),
        ("6", "Ширина машины"),
        ("7", "Длина машины "),
        ("8", "Высота машины"),
        ("9", "Вес машины"),
    ]


    VALUE_CHOICES = [
        ("1", "380 V"),
        ("2", "50 Hz"),
        ("3", "1.1 Kw"),
        ("4", "6 bar"),
        ("5", "6 It/min"),
        ("6", "660 mm"),
        ("7", "800 mm"),
        ("8", "1270 mm"),
        ("9", "150 kg")
    ]

   

    # catalog = models.ForeignKey(on_delete=models.CASCADE, null=True,  blank=True)
    # title = models.ForeignKey(on_delete=models.CASCADE, null=True,  blank=True)
    # # name = models.CharField(max_length=150)
    # categorie = models.ForeignKey('Categorie')
    # name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="atlasmak", null=True, blank=True)
    number = models.CharField(max_length=20)
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.CharField(max_length=225)
    parameter = models.CharField(max_length=20, choices=PARAMETER_CHOICES, default=1)
    parameter1 = models.CharField(max_length=20, choices=PARAMETER_CHOICES, default=2)
    parameter2 = models.CharField(max_length=20, choices=PARAMETER_CHOICES, default=3)
    parameter3 = models.CharField(max_length=20, choices=PARAMETER_CHOICES, default=4)
    parameter4 = models.CharField(max_length=20, choices=PARAMETER_CHOICES, default=5)
    parameter5 = models.CharField(max_length=20, choices=PARAMETER_CHOICES, default=6)
    parameter6 = models.CharField(max_length=20, choices=PARAMETER_CHOICES, default=7)
    parameter7 = models.CharField(max_length=20, choices=PARAMETER_CHOICES, default=8)
    parameter9 = models.CharField(max_length=20, choices=PARAMETER_CHOICES, default=9)

    
    value = models.CharField(max_length=20, choices=VALUE_CHOICES, default=1)
    value1 = models.CharField(max_length=20, choices=VALUE_CHOICES, default=2)
    value2 = models.CharField(max_length=20, choices=VALUE_CHOICES, default=3)
    value3 = models.CharField(max_length=20, choices=VALUE_CHOICES, default=4)
    value4 = models.CharField(max_length=20, choices=VALUE_CHOICES, default=5)
    value5 = models.CharField(max_length=20, choices=VALUE_CHOICES, default=6)
    value6 = models.CharField(max_length=20, choices=VALUE_CHOICES, default=7)
    value7 = models.CharField(max_length=20, choices=VALUE_CHOICES, default=8)
    value8 = models.CharField(max_length=20, choices=VALUE_CHOICES, default=9)
        

        

    # slug = models.SlugField(default='', null=False, db_index=True)
    # created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"

    def __str__(self):
        return f"{self.title} ({self.price})"



class Parameter(models.Model):
    # #name_parameter = models.CharField(max_length=150)
    # parameter = models.CharField(max_length=20, choices=PARAMETER_CHOICES, default="1")
    # catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, null=True,  blank=True)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Технические характеристики"
        verbose_name_plural = "Технические характеристики"

    # def __str__(self):
    #     return f"{self.name} ({self.value self.category})"

    def __str__(self):
        return f"{self.name} ({self.value})"


class Delivery(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Доставка"
        verbose_name_plural = "Доставки"
        ordering = ["title"]


class Contacts(models.Model):
    # title = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    addresses = models.CharField(max_length=40)
    created_on = models.DateField(auto_now_add=True)

    # url = models.URLField(blank=True)

    # def __str__(self):
    #     return self.title

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


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
