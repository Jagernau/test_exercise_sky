
from djmoney.models.fields import MoneyField
from django.db import models


class Based_Mixin(models.Model):
    class Meta:
        abstract = True
    
    title = models.CharField(verbose_name="Название", max_length=255)
    debt = MoneyField(max_digits=20, decimal_places=4, null=True, default_currency="RUB", verbose_name="Задолженность", blank=True)
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)


