from django.contrib import admin
from .models import *
from .models import Company, Catalog, Contacts, Delivery, Parameter


# admin.site.register(News)
# admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Catalog)
admin.site.register(Delivery)
admin.site.register(Contacts)
admin.site.register(Parameter)
# admin.site.register(VisitNumber)
# admin.site.register(DayNumber)
