from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price']


admin.site.register(models.Collection)
admin.site.register(models.Product, ProductAdmin)

# Register your models here.
