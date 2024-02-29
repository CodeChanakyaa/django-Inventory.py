from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action


class InventoryVS(viewsets.ViewSet):
    def list(self, request):
        inventoryitems = InventoryItem.objects.all()
        serializer = InventoryItemSerializer(inventoryitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        id = pk
        inventoryitem = InventoryItem.objects.get(id=id)
        serializer = InventoryItemSerializer(inventoryitem)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        inventoryitem = InventoryItem.objects.get(id=id)
        serializer = InventoryItemSerializer(inventoryitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        id = pk
        inventoryitem = InventoryItem.objects.get(id=id)
        inventoryitem.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['GET'])
    def short_method(self, request):
        sorteditems = InventoryItem.objects.all().order_by('-price')
        serializer = InventoryItemSerializer(sorteditems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def category_method(self, request, slug):
        category = slug
        filtereditems = InventoryItem.objects.filter(category=category)
        if filtereditems:
            serializer = InventoryItemSerializer(filtereditems, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_200_OK)
