from django.urls import path, include
from .views import *

urlpatterns = [
    path('products/', ProductList, name='product_list'),
    path('products/search_results', ProductSearchList, name='search_result'),
    path('products/create', create_product, name='create_product'),
]
