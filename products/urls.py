from django.urls import path, include
from .views import *

urlpatterns = [
    path('products/', ProductList),
    path('products/search_results', ProductSearchList),
    path('products/create', create_product),
]
