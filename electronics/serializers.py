from rest_framework import serializers

from electronics.models import AddressCompany, Contacts, Products, Provider, Stuff

from drf_writable_nested.serializers import WritableNestedModelSerializer 
from electronics.validators import validate_comparison





# Элементы

class ProductsSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class StaffSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Stuff
        fields = ("first_name", "last_name", "is_active", "password", "username", "email")

    


class AddressCompanySerializer(WritableNestedModelSerializer):
    class Meta:
        model = AddressCompany
        fields = "__all__"


class ContactsSerializer(WritableNestedModelSerializer):
    address = AddressCompanySerializer()
    class Meta:
        model = Contacts
        fields = "__all__"


class ProviderKSerializer(WritableNestedModelSerializer):
    product = ProductsSerializer()
    stuff = StaffSerializer()
    name_trade_network = serializers.IntegerField(validators=[validate_comparison], help_text="select 0 or 1")
    contacts = ContactsSerializer()

    class Meta:
        model = Provider
        fields = "__all__"



class ProviderUpdateSerialiser(ProviderKSerializer):
    """ 
    Делает задолженность только для чтения в update
    """
    class Meta:
        read_only_fields = ("debt",)
        model = Provider
        fields = "__all__"


class ProviderListSerialiser(ProviderKSerializer):
    """
    Сериализтор с изменением поля name_trade_network с выводом не int а названия
    """
    name_trade_network = serializers.CharField(source="get_name_trade_network_display")
    class Meta:
        model = Provider
        fields = "__all__"


