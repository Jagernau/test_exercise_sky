

from rest_framework import viewsets

from electronics.models import TradingNetwork
from electronics.serializers import NetworKSerializer
from rest_framework.response import Response



# class NetworkListView(ListAPIView):
#     model = TradingNetwork
#     serializer_class = NetworKSerializer
#     queryset = TradingNetwork.objects.all()


class ProviderCRUD(viewsets.ModelViewSet):
        queryset = TradingNetwork.objects.all()
        serializer_class = NetworKSerializer
