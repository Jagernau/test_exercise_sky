

from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from electronics.models import TradingNetwork, Provider
from electronics.permissions import ActivePermission
from electronics.serializers import ProviderKSerializer, ProviderUpdateSerialiser
from rest_framework.response import Response



# class NetworkListView(ListAPIView):
#     model = TradingNetwork
#     serializer_class = NetworKSerializer
#     queryset = TradingNetwork.objects.all()


class ProviderCRUD(viewsets.ModelViewSet):
        queryset = Provider.objects.all()
        serializer_class = ProviderKSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        filterset_fields = ('contacts__address__country',)
        permission_classes = [IsAuthenticated,ActivePermission]

        def get_serializer_class(self):
            if self.action == "update":
                return ProviderUpdateSerialiser

            return ProviderKSerializer
