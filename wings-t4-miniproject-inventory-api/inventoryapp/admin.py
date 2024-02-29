from django.contrib import admin
from .models import *

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']
    
@admin.register(InventoryItem)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'quantity', 'barcode']