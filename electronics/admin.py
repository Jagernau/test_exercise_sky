from django import forms
from django.contrib import admin
from django.db.models import QuerySet

from electronics.models import TradingNetwork, Products, Provider
from django.contrib import admin





@admin.action(description='Удалить задолженность')
def del_bebt(modeladmin, request, queryset: QuerySet):
    queryset.update(debt=None)

    
class ImageAdminInline(admin.TabularInline):
        extra = 1
        model = Products


class NetworAdmine(admin.ModelAdmin):
    list_display = ("title", "provider")
    list_display_links = ("title", "provider")
    actions = [del_bebt, ]
    list_filter = ('contacts__address__country',)
    list_select_related = True
#    inlines = (ImageAdminInline,)

admin.site.register(TradingNetwork, NetworAdmine)
admin.site.register(Products)


