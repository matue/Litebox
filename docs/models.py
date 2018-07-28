from django.db import models
from products.models import CommonModel, Product
from shops.models import Shop
from users.models import Person
from django.contrib.auth.models import User


class DocType(CommonModel):
    doc_type_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % self.doc_type_name

    class Meta:
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Типы документов'


class Document(CommonModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, default=None)
    doc_type = models.ForeignKey(DocType, on_delete=models.CASCADE, default=None)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField('Date', default=None)

    def __str__(self):
        return 'Дата: %s, Магазин: %s' % (self.date, self.shop.shop_name)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class ProductsInDoc(CommonModel):  # промежуточная модель, связывает продукты и документы для указания количества продуктов в документе
    document = models.ForeignKey(Document, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1, null=False, blank=False)

    def __str__(self):
        return 'Продукт: %s, Документ: %s' % (self.product.product_name, self.document.doc_type)

    class Meta:
        verbose_name = 'Запись в документе'
        verbose_name_plural = 'Записи в документе'