from django.contrib import admin

from .models import (
    IceCreamOrder
)

@admin.register(IceCreamOrder)
class IceCreamOrder(admin.ModelAdmin):
    list_display = ['flavor']