from django.contrib import admin
from . import models
from .models import Category, News, Company, Certificate, Catalog, Delivery

admin.site.register(Category)
admin.site.register(News)
admin.site.register(Company)
admin.site.register(Certificate)
admin.site.register(Catalog)
admin.site.register(Delivery)


