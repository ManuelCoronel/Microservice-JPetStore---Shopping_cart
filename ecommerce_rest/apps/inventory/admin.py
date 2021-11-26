from django.contrib import admin
from apps.inventory.models import Category,Product,Item


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Item)
