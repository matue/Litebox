from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from users.models import Person
from .serializers import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@login_required
def DocList(request):
    queryset = Document.objects.all()
    shops = Shop.objects.all()
    doctypes = DocType.objects.all()
    persons = Person.objects.all()
    count=0
    return render(request, 'doc_list.html', {'object_list': queryset,
                                                  'shops': shops,
                                                  'doctypes': doctypes,
                                                  'persons': persons, 'count': count})


@login_required
def DocSearchList(request):
    filter_value = request.POST
    doctypes = DocType.objects.all()
    shops = Shop.objects.all()
    persons = Person.objects.all()
    doc_type_id = filter_value.get('doc_type_id')
    person_id = filter_value.get('person_id')
    shop_id = filter_value.get('shop_name')
    begin_date = filter_value.get('begin_date')
    end_date = filter_value.get('end_date')
    query = "SELECT * FROM DOCS_DOCUMENT WHERE DOC_TYPE_ID = %s AND PERSON_ID = %s AND SHOP_ID = %s AND DATE BETWEEN TO_DATE(%s,'YYYY-MM-DD') AND TO_DATE(%s,'YYYY-MM-DD')"
    queryset = Document.objects.raw(query, [doc_type_id, person_id, shop_id, begin_date, end_date])
    return render(request, 'doc_search_results.html', {'object_list': queryset,
                                                       'shops': shops,
                                                       'doctypes': doctypes,
                                                       'persons': persons})


@login_required
def Doc(request, id):
    queryset = ProductsInDoc.objects.filter(document=id)
    doc_info = Document.objects.filter(id=id)
    products = Product.objects.all()
    return render(request, 'doc.html', {'object_list': queryset,
                                             'doc_info': doc_info,
                                             'products': products,
                                             'doc_id': id})


@login_required
@csrf_exempt
def add_product_to_doc(request):
    if request.method == 'POST':
        data = request.POST
        serializer = ProductsInDocSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@login_required
@csrf_exempt
def add_doc(request):
    if request.method == 'POST':
        data = request.POST
        serializer = DocSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class docs_api_test(APIView):

    def get(self, request, format=None):
        docs = Document.objects.all()
        serializer = DocSerializer(docs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DocSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)