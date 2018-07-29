from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required
def ProductList(request):
    queryset = Product.objects.all()
    measures = Measure.objects.all()
    return render(request, 'product_list.html', {'object_list': queryset,
                                                 'measures': measures})

@login_required
def ProductSearchList(request):
    search_value = request.POST
    product_name = search_value.get('product_name')
    queryset = Product.objects.filter(product_name__contains=product_name)
    return render(request, 'product_search_results.html', {'object_list': queryset})


@login_required
@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = request.POST
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)