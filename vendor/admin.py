from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['__str__','slug']
    class Meta:
        models=Product

admin.site.register(Product,ProductAdmin)
