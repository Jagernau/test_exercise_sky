from django.contrib import admin

from electronics.models import TradingNetwork, Products
from django.contrib import admin
from django_reverse_admin import ReverseModelAdmin

class NetworAdmine(ReverseModelAdmin):
    inline_reverse = ["product", "stuff"]
    inline_type = 'tabular'

admin.site.register(TradingNetwork, NetworAdmine)
