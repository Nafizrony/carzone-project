from django.shortcuts import render
from .models import Team
# Create your views here.

def home(request):
    team_members = Team.objects.all()
    context = {'team_members':team_members}
    return render(request,'pages/home.html',context)

def cars(request):
    context = {}
    return render(request,'pages/cars.html',context)

def about(request):
    context = {}
    return render(request,'pages/about.html',context)

def services(request):
    context = {}
    return render(request,'pages/services.html',context)

def contact(request):
    context = {}
    return render(request,'pages/contact.html',context)
