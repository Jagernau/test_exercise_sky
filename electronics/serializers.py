from rest_framework import serializers

from electronics.models import AddressCompany, Contacts, TradingNetwork, Products, Provider
from users.models import User







# Элементы
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name")


class AddressCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressCompany
        fields = "__all__"


class ContactsSerializer(serializers.ModelSerializer):
    address = AddressCompanySerializer(read_only=True)
    class Meta:
        moel = Contacts
        fields = "__all__"


class ProviderKSerializer(serializers.ModelSerializer):
    product = ProductsSerializer(many=True)
    stuff = StaffSerializer(read_only=True)
    name_trade_network = serializers.CharField(source='get_name_trade_network_display')
    class Meta:
        model = Provider
        fields = "__all__"




# Сериализатор цепочки
class NetworKSerializer(serializers.ModelSerializer):
    product = ProductsSerializer(read_only=True)
    stuff = StaffSerializer(read_only=True)
    name_trade_network = serializers.CharField(source='get_name_trade_network_display')
    provider = ProviderKSerializer(read_only=True)
    class Meta:
        model = TradingNetwork
        fields = "__all__"

