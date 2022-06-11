from django.contrib import admin
from .models import Product
from . import models

# Register your models here.

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'brand', 'title', 'slug', 'description', 'image', 'price', 'available']
    list_filter = ['category']
    list_editable = ['price', 'available']
    # prepopulated_fields = {'slug': ('name',)}


#     def get_img(self, obj):
#         if obj.cms_img:
#             return mark_safe(f'<img src="{obj.cms_img.url}" width="80px"')
#         else:
#             return 'нет картинки'

#     get_img.short_description = 'Миниатюра'

# phone.png
admin.site.register(News)
admin.site.register(Company)
admin.site.register(Certificate)
admin.site.register(Catalog)
admin.site.register(Delivery)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(News)

