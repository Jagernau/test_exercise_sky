
from django.db import models
from electronics.mixins import Based_Mixin
from users.models import User



# Продукты
class Products(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    model = models.CharField(verbose_name="Модель", max_length=255)
    launch_date = models.DateField(verbose_name="Дата выпуска")
    class Meta:       
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
  

# Адрес
class AddressCompany(models.Model):
    country = models.CharField(verbose_name="Страна", max_length=100)
    town = models.CharField(verbose_name="Город", max_length=100)
    street = models.CharField(verbose_name="Улица", max_length=100)
    house_number = models.IntegerField(verbose_name="Номер дома")


# Контакты
class Contacts(models.Model):
    email = models.EmailField(verbose_name="Почта", max_length=100)
    address = models.ForeignKey("AddressCompany", on_delete=models.PROTECT, verbose_name="Адрес")




# Сеть



class TradingNetwork(Based_Mixin):
    class Meta:       
        verbose_name = "Сеть"
        verbose_name_plural = "Сети"

    class Name(models.IntegerChoices):
        fabric = 0, "Завод"
        distributor = 1, "Дистрибьютер"
        dealership = 2, "Диллер"
        retail_chain = 3, "Розница"
        entrepreneur = 4, "Предприниматель"

    name_trade_network = models.PositiveSmallIntegerField(verbose_name="Звено цепи", choices=Name.choices)
    contacts = models.ForeignKey("Contacts", on_delete=models.CASCADE, null=False)
    product = models.ForeignKey("Products", on_delete=models.CASCADE, null=False)
    stuff = models.ForeignKey(User, on_delete=models.CASCADE)
#    provider = None # Поставщик

