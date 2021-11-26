from django.urls import path
from apps.shopping_cart.api.api import shopping_cart_list
urlpatterns = [
    path('cart/',shopping_cart_list,name='cart'),

  #  path('item/',ItemAPIView.as_view(),name='categoria_api'),
]
