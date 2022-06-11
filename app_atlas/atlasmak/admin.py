from django.contrib import admin

from django.utils.safestring import mark_safe

from .models import *


#  list_display = ('news_title')
#     list_display_links = ('news_title',)
#     list_editable = ('')
#     fields = ('')
#     readonly_fields = ('news_img',)

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
