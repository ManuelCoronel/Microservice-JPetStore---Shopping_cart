from rest_framework.views import APIView
from apps.shopping_cart.api.serializers import ShoppingCartSerializer
from rest_framework.decorators import api_view
from apps.shopping_cart.models import Shopping_cart
from rest_framework.response import Response


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

@api_view(['GET','PUT','DELETE'])
def shopping_cart_detail(request, addresS):
    if request.method == 'GET':
        shopping_cart = Shopping_cart.objects.get(addres=addresS)
        serializer = ShoppingCartSerializer(shopping_cart)
        return Response(serializer.data)
    if request.method == 'PUT':
        shopping_cart = Shopping_cart.objects.get(addres=addresS)
        serializer = ShoppingCartSerializer(shopping_cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        shopping_cart = Shopping_cart.objects.get(addres=addresS)
        shopping_cart.delete()
        return Response(status=204)