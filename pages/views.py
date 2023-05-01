from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
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
