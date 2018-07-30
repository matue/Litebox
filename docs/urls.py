from django.urls import path, include
from .views import *

urlpatterns = [
path('docs/', DocList),
    path('docs/<int:id>', Doc),
    path('docs/addproduct', add_product_to_doc),
    path('docs/adddoc', add_doc),
    path('docs/search_results', DocSearchList),
    # path('docs/api', docs_api_test.as_view()),
]
