from django.contrib import admin
from .models import *


class ProductsInDocInline(admin.TabularInline):  # добавляем в админку возможность указывать товары в документе
    model = ProductsInDoc
    extra = 0  # дополнительные ряды для добавления


class DocumentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Document._meta.fields]
    inlines = [ProductsInDocInline]


admin.site.register(DocType)
admin.site.register(Document, DocumentAdmin)