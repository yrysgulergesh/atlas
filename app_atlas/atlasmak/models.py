from amplitude import Amplitude
from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField, ImageField
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from hitcount.models import HitCount
from hitcount.views import HitCountDetailView, HitCountMixin


class Catalog(models.Model, HitCountMixin):
    image = models.ImageField(upload_to="atlasmak", null=True, blank=True)
    number = models.CharField(max_length=20)
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.CharField(max_length=225)

    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"

    def __str__(self):
        return f"{self.title} ({self.price})"


class Parameter(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Технические характеристики"
        verbose_name_plural = "Технические характеристики"

    def __str__(self):
        return f"{self.name} ({self.value})"


class Company(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        verbose_name = "О компании"
        verbose_name_plural = "О компании"
        ordering = ["title"]

    def __str__(self):
        return self.title


# class Certificate(models.Model):
#     photo = models.ImageField(upload_to = "atlasmak", null=True, blank=True)


#     class Meta:
#         verbose_name ='Сертификаты качества'
#         verbose_name_plural = 'Сертификаты качества'
#         ordering = ['photo']


class Delivery(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    class Meta:
        verbose_name = "Доставка"
        verbose_name_plural = "Доставки"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Contacts(models.Model):
    phone = models.CharField(max_length=40)
    addresses = models.CharField(max_length=150)

    # url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.title
