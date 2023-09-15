from django.contrib import admin
from .models import Clients, Products, Orders


admin.site.register(Clients)
admin.site.register(Products)


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    filter_vertical = ['name_product']