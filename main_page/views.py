from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'home.html')

def inquire(request):
    return render(request, "inquire.html")

def H_car_recap(request):
    return render(request, "H_car_recap.html")

def Related_Sites(request):
    return render(request, "Related_Sites.html")