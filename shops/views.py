from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# @login_required
def ShopList(request):
    queryset = Shop.objects.all()
    return render(request, 'shop_list.html', {'object_list': queryset})


# @login_required
def ShopSearchList(request):
    search_value = request.POST
    shop_name = search_value.get('shop_name')
    queryset = Shop.objects.filter(shop_name__contains=shop_name)
    return render(request, 'shop_search_results.html', {'object_list': queryset})


# @login_required
@csrf_exempt
def create_shop(request):
    if request.method == 'POST':
        data = request.POST
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
