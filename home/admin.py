"""Admin configuration for home app models."""

# pylint: disable=missing-class-docstring, wildcard-import, unused-wildcard-import

from django.contrib import admin
from .models import *


class LocationAdmin(admin.ModelAdmin):
    """Admin configuration for Location model."""
    list_display = ('city',)


class CarDealerAdmin(admin.ModelAdmin):
    """Admin configuration for CarDealer model."""
    list_display = ('car_dealer', 'phone', 'location', 'earnings', 'type')


class CarAdmin(admin.ModelAdmin):
    """Admin configuration for Car model."""
    list_display = ('name', 'img_preview', 'car_dealer', 'capacity', 'location', 'is_available', 'rent')


class CustomerAdmin(admin.ModelAdmin):
    """Admin configuration for Customer model."""
    list_display = ('user', 'phone', 'location', 'type')


class OrderAdmin(admin.ModelAdmin):
    """Admin configuration for Order model."""
    list_display = ('user', 'car_dealer', 'car', 'rent', 'days', 'is_complete')


admin.site.register(Location, LocationAdmin)
admin.site.register(CarDealer, CarDealerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
