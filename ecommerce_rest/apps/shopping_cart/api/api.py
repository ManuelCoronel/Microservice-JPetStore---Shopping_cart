from rest_framework.views import APIView
from apps.shopping_cart.api.serializers import ShoppingCartSerializer,ShoppingCartSerializerWithout
from rest_framework.decorators import api_view
from apps.shopping_cart.models import Shopping_cart
from rest_framework.response import Response


@api_view(['GET','POST','DELETE'])
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
    elif request.method == 'DELETE':
        customer_id = request.GET.get('customerId')
        itemId = int(request.GET.get('item_id'))
        print(customer_id)
        print(itemId)

        shopping_cart = Shopping_cart.objects.filter(customerId=customer_id,item_id=itemId)
        print(shopping_cart)
        shopping_cart.delete()
        return Response(status=204)

@api_view(['GET'])   
def shopping_cart_de(request):
    if request.method == 'GET':
        shopping_cart = Shopping_cart.objects.all()
        serializer = ShoppingCartSerializer(shopping_cart, many=True)
        return Response(serializer.data)

@api_view(['GET','PUT'])
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