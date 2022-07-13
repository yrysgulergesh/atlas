from django.contrib import admin
from . import models
from .models import Company, Catalog, Delivery, Specification


# admin.site.register(News)
admin.site.register(Company)
admin.site.register(Catalog)
admin.site.register(Delivery)
admin.site.register(Specification)
# admin.site.register(DayNumber)

