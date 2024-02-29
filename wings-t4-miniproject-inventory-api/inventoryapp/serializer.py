from rest_framework import serializers
from .models import *

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['name']


class InventoryItemSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'category', 'price', 'discount', 'quantity', 'barcode']
