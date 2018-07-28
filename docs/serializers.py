from rest_framework import serializers
from .models import Document, ProductsInDoc


class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('shop', 'doc_type', 'person', 'date')


class ProductsInDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsInDoc
        fields = ('product', 'document', 'amount')
