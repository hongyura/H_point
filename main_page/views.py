from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'home.html')

def inquire(request):
    return render(request, "inquire.html")

<<<<<<< HEAD
def H_car_recap(request):
    return render(request, "H_car_recap.html")

def Related_Sites(request):
    return render(request, "Related_Sites.html")
=======
def H_car_charge(request):
    return render(request, "H_car_charge.html")

>>>>>>> cdbcfd7e6b324b3bf7929b798ccbbcf81d63e64b
