from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def inquire(request):
    return render(request, "inquire.html")

def H_car_recap(request):
    return render(request, "H_car_recap.html")

def Related_Sites(request):
    return render(request, "Related_Sites.html")

def H_car_charge(request):
    return render(request, "H_car_charge.html")

def what_H_point(request):
    return render(request, "what_H_point.html")

def participate(request):
    return render(request, "participate.html")


def prediction(request):
    return render(request, "prediction.html")

def material(request):
    return render(request, "material.html")

def press_release(request):
    return render(request, "press_release.html")


def point_payment(request):
    return render(request, "point_payment.html")
