from rest_framework import serializers

from electronics.models import AddressCompany, Contacts, TradingNetwork, Products
from users.models import User


# Элементы
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AddressCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressCompany
        fields = "__all__"


class ContactsSerializer(serializers.ModelSerializer):
    address = AddressCompanySerializer(many=True)
    class Meta:
        moel = Contacts
        fields = "__all__"




# Сериализатор цепочки
class NetworKSerializer(serializers.ModelSerializer):
    product = ProductsSerializer(many=True)
    stuff = StaffSerializer(many=True)
    
    class Meta:
        model = TradingNetwork
        fields = "__all__"

