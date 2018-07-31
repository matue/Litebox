from django.urls import path, include
from .views import *

urlpatterns = [
    path('docs/', DocList, name='doc_list'),
    path('docs/<int:id>', Doc, name='Doc'),
    path('docs/addproduct', add_product_to_doc, name='add_product'),
    path('docs/adddoc', add_doc, name='add_doc'),
    path('docs/search_results', DocSearchList, name='doc_search'),
    path('docs/api', docs_api_test.as_view()),
]
