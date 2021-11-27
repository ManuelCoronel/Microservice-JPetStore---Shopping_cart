from django.urls import path
from apps.shopping_cart.api.api import shopping_cart_list, shopping_cart_detail,shopping_cart_de

urlpatterns = [
    path('cart/',shopping_cart_list,name='cart'),
    path('cart/<str:addresS>/',shopping_cart_detail,name='cart'),
    path('cart/clear/<str:addresS>/',shopping_cart_detail,name='cart'),
   
  #  path('item/',ItemAPIView.as_view(),name='categoria_api'),
]
