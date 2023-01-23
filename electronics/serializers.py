from rest_framework import serializers

from electronics.models import AddressCompany, Contacts, Products, Provider, Stuff

from drf_writable_nested.serializers import WritableNestedModelSerializer 






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
    name_trade_network = serializers.IntegerField()
    contacts = ContactsSerializer()

    class Meta:
        model = Provider
        fields = "__all__"



class ProviderUpdateSerialiser(ProviderKSerializer):
    class Meta:
        read_only_fields = ("debt",)
        model = Provider
        fields = "__all__"



# # Сериализатор цепочки
# class NetworKSerializer(serializers.ModelSerializer):
#     product = ProductsSerializer(read_only=True)
#     stuff = StaffSerializer(read_only=True)
#     name_trade_network = serializers.CharField(source='get_name_trade_network_display')
#     provider = ProviderKSerializer(read_only=True)
#     class Meta:
#         model = TradingNetwork
#         fields = "__all__"
#
