from django.contrib import admin
from django.urls import include, path, re_path as url
from inventoryapp.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('inventory/items', InventoryVS, basename='inventory')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),

    path('items/sort/', InventoryVS.as_view({'get': 'short_method'})),

    url(r'^items/query/(?P<slug>[\D+]+)/$',
        InventoryVS.as_view({'get': 'category_method'})),
]
