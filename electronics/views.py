

from rest_framework import viewsets

from electronics.models import TradingNetwork, Provider
from electronics.serializers import NetworKSerializer, ProviderKSerializer, ProviderUpdateSerialiser
from rest_framework.response import Response



# class NetworkListView(ListAPIView):
#     model = TradingNetwork
#     serializer_class = NetworKSerializer
#     queryset = TradingNetwork.objects.all()


class ProviderCRUD(viewsets.ModelViewSet):
        queryset = Provider.objects.all()
        serializer_class = ProviderKSerializer

        def get_serializer_class(self):
            if self.action == "update":
                return ProviderUpdateSerialiser

            return ProviderKSerializer
