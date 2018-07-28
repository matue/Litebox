from django.urls import path, include
from .views import *


urlpatterns = [
    path('shops/', ShopList),
    path('shops/search_results', ShopSearchList),
    path('shops/create', create_shop),
]
