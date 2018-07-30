from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from docs.views import add_string

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


@csrf_exempt
def create_product(request):
    add_string(request, ProductSerializer)



