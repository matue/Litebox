from django.db import models
from model_utils.models import TimeStampedModel  # django-model-utils package


class Measure(TimeStampedModel):
    measure_name = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return '%s' % self.measure_name

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'


class Product(TimeStampedModel):
    product_name = models.CharField(max_length=100, blank=False)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE, default='1')
    barcode = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return '%s' % self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('product_name', 'barcode')  # сортировка объектов по имени

