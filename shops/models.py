from django.db import models
from model_utils.models import TimeStampedModel


class Shop(TimeStampedModel):
    shop_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return '%s' % self.shop_name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

