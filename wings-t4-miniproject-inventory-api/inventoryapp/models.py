from django.db import models

# another way of implementing category
# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    # category = models.ForeignKey(Category, related_name='inventory_items', on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField()
    discount = models.IntegerField()
    barcode = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

    # @classmethod
    # def category_filter(cls, category):
    #     return cls.objects.filter(category__name=category)
