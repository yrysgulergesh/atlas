from django.db import models
from django.forms import ImageField


from django.db import models
from django.db.models.signals import pre_save  # для автозаполнения поля slug
from django.utils.text import slugify
from django.urls import reverse
from transliterate import translit  # get_available_language_codes    #  для перевода имя категории


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(blank=True, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})  # делает ссылки


def pre_save_category_slug(sender, instance, *args, **kwargs):  # для автозаполнения и перевода ссылок
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug


pre_save.connect(pre_save_category_slug, sender=Category)


class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]  # для названия картинки
    return '{0}/{1}'.format(instance.slug, filename)


class ProductManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд')
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(blank=True)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to=image_folder, verbose_name='Изображение')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    objects = ProductManager()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title']  # сортировка по имени

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # делает ссылки
        return reverse('product_detail', kwargs={'product_slug': self.slug})


def pre_save_product_slug(sender, instance, *args, **kwargs):  # для автозаполнения ссылок
    if not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug


pre_save.connect(pre_save_product_slug, sender=Product)


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Новости сайта')
    content = models.TextField(blank=True, verbose_name='Текст')
    created_at = models.DateField(auto_now_add=True, verbose_name='Добавить')
    updated_at = models.DateField(auto_now=True, verbose_name='Обновить')
    # delete_at = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Удалить')
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