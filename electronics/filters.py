import django_filters

from electronics.models import Provider



class CountryFilter(django_filters.rest_framework.FilterSet):
    contacts = django_filters.CharFilter("contacts__address__country", lookup_expr='iexact')
    class Meta:
        model = Provider
        fields = ["title",]
