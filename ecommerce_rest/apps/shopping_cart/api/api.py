from rest_framework.views import APIView
from apps.shopping_cart.api.serializers import ShoppingCartSerializer,ShoppingCartSerializerWithout
from rest_framework.decorators import api_view
from apps.shopping_cart.models import Shopping_cart
from rest_framework.response import Response
import json

@api_view(['GET','POST'])
def shopping_cart_list(request):
    
    if request.method == 'GET':
        shopping_cart = Shopping_cart.objects.all()
        serializer = ShoppingCartSerializer(shopping_cart, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ShoppingCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# ELIMINA UN ITEM DEL CARRITO SEGUN EL CORREO Y EL ID DEL ITEM
@api_view(['DELETE'])   
def shopping_cart_delete_detail(request, addresS,item_id):
    if request.method == 'DELETE':
        shopping_cart = Shopping_cart.objects.filter(customerId=addresS,item_id=item_id)
        Shopping_cart.delete()
        return Response(status=204)


@api_view(['GET','PUT','DELETE'])
def shopping_cart_detail(request, addresS):
    if request.method == 'GET':
        shopping_cart = Shopping_cart.objects.filter(customerId=addresS)
        print(shopping_cart.__str__())
        serializer = ShoppingCartSerializerWithout(shopping_cart,many=True)
        return Response(serializer.data)
    if request.method == 'PUT':
        shopping_cart = Shopping_cart.objects
        serializer = ShoppingCartSerializerWithout(shopping_cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    if request.method == 'DELETE':
        shopping_cart = Shopping_cart.objects.filter(customerId=addresS)
        shopping_cart.delete()
        return Response(status=204)



@api_view(['DELETE'])
def shopping_cart_del(request, addresS,item_id=None):
    if request.method == 'DELETE':
        shopping_cart = Shopping_cart.objects.filter(customerId=addresS, item_id=item_id)
        shopping_cart.delete()
        return Response(status=204)



@api_view(['DELETE'])
def shopping_cart_clear(request, addresS):
    if request.method == 'DELETE':
        shopping_cart = Shopping_cart.objects.filter(customerId=addresS)
        shopping_cart.delete()
        return Response(status=204)

@api_view(['GET'])
def shopping_cart_count(request, addresS):
    if request.method == 'GET':
        shopping_cart = len(Shopping_cart.objects.filter(customerId=addresS))
    data = {
        'count': shopping_cart
    }
    return Response(data)