from django.shortcuts import render
from .models import Brand, Car

def home(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    return render(request, 'main/home.html', {'brands': brands, 'cars': cars})

def brand_detail(request, brand_id):
    brand = Brand.objects.get(pk=brand_id)
    cars = brand.cars.all()
    return render(request, 'main/brand_detail.html', {'brand': brand, 'cars': cars})
