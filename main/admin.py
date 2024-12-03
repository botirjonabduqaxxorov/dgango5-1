from django.contrib import admin
from .models import Brand, Car

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'brand', 'price', 'year', 'color')
    list_filter = ('brand', 'year', 'color')
