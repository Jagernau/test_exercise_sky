
from django.db import models


class Based_Mixin(models.Model):
    class Meta:
        abstract = True
    
    title = models.CharField(verbose_name="Название", max_length=255)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)


