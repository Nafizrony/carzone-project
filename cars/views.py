from django.shortcuts import render
from .models import *
# Create your views here.

def cars(request):
    features_cars = Cars.objects.filter(is_featured=True)
    context = {'features_cars':features_cars}
    return render(request,'cars/cars.html',context)