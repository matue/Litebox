from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('', include('shops.urls')),
    path('', include('docs.urls')),
    path('', include('users.urls')),
]
