

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from electronics.models import TradingNetwork
from electronics.serializers import NetworKSerializer



class NetworkListView(ListAPIView):
    model = TradingNetwork
    serializer_class = NetworKSerializer
    queryset = TradingNetwork.objects.all()



