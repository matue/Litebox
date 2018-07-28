from django.db import models


class CommonModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Measure(CommonModel):
    measure_name = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return '%s' % self.measure_name

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'


class Product(CommonModel):
    product_name = models.CharField(max_length=100, blank=False)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE, default='1')
    barcode = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return '%s' % self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('product_name', 'barcode')  # сортировка объектов по имени


