from rest_framework.views import APIView
from apps.inventory.api.serializers import CategorySerializer, ProductSerializer, ItemSerializer, ProductSimpleSerializer, ItemSimpleSerializer
from rest_framework.decorators import api_view
from apps.inventory.models import Category, Product, Item
from rest_framework.response import Response
from drf_extra_fields.fields import Base64ImageField
import json


@api_view(['GET','POST'])
def category_api_view(request):
    if request.method == 'GET':
        categorys =  Category.objects.all()
        categorys_serializer = CategorySerializer(categorys,many=True)
        return Response(categorys_serializer.data)

    elif request.method == 'POST':
        category_serializer = CategorySerializer(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data)
        return Response(category_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def category_detail_view(request,pk=None):
    if request.method == 'GET':
        category = Category.objects.filter(id = pk).first()
        category_serializer = CategorySerializer(category)
        return Response(category_serializer.data)
    
    elif request.method == 'PUT':
        category = Category.objects.filter(id = pk).first()
        category_serializer = CategorySerializer(category,data = request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data)
        return Response(category_serializer.errors)
    
    elif request.method == 'DELETE':
        category = Category.objects.filter(id = pk).first()
        category.delete()
        return Response('Eliminado')


@api_view(['GET','POST'])
def product_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products,many=True)
        return Response(products_serializer.data)
        
    elif request.method == 'POST':
         products_serializer = ProductSimpleSerializer(data=request.data)
         if  products_serializer.is_valid():
            products_serializer.save()
            return Response( products_serializer.data)
    return Response( products_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def product_detail_view(request,pk=None):
    if request.method == 'GET':
        product = Product.objects.filter(id = pk).first()
        product_serializer = ProductSerializer(product)
        return Response(product_serializer.data)
    
    elif request.method == 'PUT':
        product = Product.objects.filter(id = pk).first()
        product_serializer = ProductSerializer(product,data = request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)
        return Response(product_serializer.errors)
    
    elif request.method == 'DELETE':
        product = Product.objects.filter(id = pk).first()
        product.delete()
        return Response('Eliminado')


@api_view(['GET','POST'])
def item_api_view(request):
    if request.method == 'GET':
        items = Item.objects.all()
        items_serializer = ItemSerializer(items,many=True)
        return Response(items_serializer.data)
        
    elif request.method == 'POST':
         items_serializer = ItemSimpleSerializer(data=request.data)
         if  items_serializer.is_valid():
            items_serializer.save()
            return Response( items_serializer.data)
    return Response( items_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def item_detail_view(request,pk=None):
    if request.method == 'GET':
        item = Item.objects.filter(id = pk).first()
        item_serializer = ItemSerializer(item)
        return Response(item_serializer.data)
    
    elif request.method == 'PUT':
        item = Item.objects.filter(id = pk).first()
        data = request.data
        data['quantity'] = item.quantity - data['quantity']
        item_serializer = ItemSerializer(item,data = request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response(item_serializer.data)
        return Response(item_serializer.errors)
    
    elif request.method == 'DELETE':
        item = Item.objects.filter(id = pk).first()
        item.delete()
        return Response('Eliminado')

class Count_products(APIView):
    def get(self, request,format=None):
        data = {
            'cantidad' :len(Product.objects.all())}
        return Response(json.dumps(data))

class Count_categories(APIView):
    def get(self, request,format=None):
        data = {
            'cantidad' :len(Category.objects.all())}
        return Response(json.dumps(data))    
        
class Count_items(APIView):
    def get(self, request,format=None):
        data = {
            'cantidad' :len(Item.objects.all())}
        return Response(json.dumps(data))