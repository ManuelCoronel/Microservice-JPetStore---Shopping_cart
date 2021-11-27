from django.db.models import fields
from rest_framework import serializers
from apps.shopping_cart.models import Shopping_cart

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping_cart
        fields = '__all__'

class ShoppingCartSerializerWithout(serializers.ModelSerializer):
    class Meta:
        model = Shopping_cart
        fields = ('item_id','quantity','price')
        
            