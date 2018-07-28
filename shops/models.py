from django.db import models
from products.models import CommonModel


class Shop(CommonModel):
    shop_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return '%s' % self.shop_name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

