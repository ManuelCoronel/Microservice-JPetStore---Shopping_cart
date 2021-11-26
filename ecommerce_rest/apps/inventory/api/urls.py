from django.urls import path
from apps.inventory.api.api import category_api_view,category_detail_view, product_api_view, product_detail_view,item_api_view,item_detail_view,Count_products, Count_items,Count_categories

urlpatterns = [
    path('category/',category_api_view,name='categoria_api'),
    path('count_products/',Count_products.as_view(),name='count_products'),
    path('count_items/',Count_items.as_view(),name='count_items'),
    path('count_categories/',Count_categories.as_view(),name='count_categories'),
    path('category/<int:pk>/',category_detail_view,name='categoria_detail_api'),
    path('product/',product_api_view ,name='producto_api'),
    path('product/<int:pk>/',product_detail_view,name='producto_detail_api'),
    path('item/',item_api_view ,name='producto_api'),
    path('item/<int:pk>/',item_detail_view,name='producto_detail_api'),
    
  #  path('item/',ItemAPIView.as_view(),name='categoria_api'),
]
