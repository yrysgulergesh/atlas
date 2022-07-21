from django.contrib import admin

from .models import *
from .models import Catalog, Company, Contacts, Delivery, Parameter

# admin.site.register(Category)
admin.site.register(Company)
# admin.site.register(Catalog)
admin.site.register(Delivery)
admin.site.register(Contacts)
# admin.site.register(Parameter)
# admin.site.register(VisitNumber)
# admin.site.register(DayNumber)




class ParameterAdmin(admin.StackedInline):
    model = Parameter


class CatalogAdmin(admin.ModelAdmin):
    inlines = [
        ParameterAdmin,
    ]


list_display = ("image", "number", "title", "description", "price")

admin.site.register(Catalog, CatalogAdmin)
