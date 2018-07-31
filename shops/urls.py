from django.urls import path, include
from .views import *


urlpatterns = [
    path('shops/', ShopList, name='shop_list'),
    path('shops/search_results', ShopSearchList, name='search_result'),
    path('shops/create', create_shop, name='create_shop'),
]
