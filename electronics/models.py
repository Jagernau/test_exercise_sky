
from django.db import models
from electronics.mixins import Based_Mixin
from users.models import User



# Продукты
class Products(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255, blank=True)
    model = models.CharField(verbose_name="Модель", max_length=255, blank=True)
    launch_date = models.DateField(verbose_name="Дата выпуска", blank=True)
    class Meta:       
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
  

# Адрес
class AddressCompany(models.Model):
    country = models.CharField(verbose_name="Страна", max_length=100, blank=True)
    town = models.CharField(verbose_name="Город", max_length=100, blank=True)
    street = models.CharField(verbose_name="Улица", max_length=100, blank=True)
    house_number = models.IntegerField(verbose_name="Номер дома", blank=True)


# Контакты
class Contacts(models.Model):
    email = models.EmailField(verbose_name="Почта", max_length=100, blank=True)
    address = models.ForeignKey("AddressCompany", on_delete=models.PROTECT, verbose_name="Адрес", blank=True)






class Provider(Based_Mixin):
    class Meta:       
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    class Name(models.IntegerChoices):
        fabric = 0, "Завод"
        retail_chain = 1, "Розница"

    name_trade_network = models.PositiveSmallIntegerField(verbose_name="Звено цепи", choices=Name.choices)
    contacts = models.ForeignKey("Contacts", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Контакты")
    product = models.ForeignKey("Products", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Продукция")
    stuff = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Работники")


    def __str__(self):
        return self.title


# Сеть



class TradingNetwork(Based_Mixin):
    class Meta:       
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"

    class Name(models.IntegerChoices):
        retail_chain = 0, "Розница"
        entrepreneur = 1, "Предприниматель"

    name_trade_network = models.PositiveSmallIntegerField(verbose_name="Звено цепи", choices=Name.choices)
    contacts = models.ForeignKey("Contacts", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Контакты")
    product = models.ForeignKey("Products", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Продукция")
    stuff = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Работники")
    provider = models.ForeignKey("Provider", on_delete=models.CASCADE, verbose_name="Поставщик", blank=True, null=True)

    def __str__(self):
        return self.title



