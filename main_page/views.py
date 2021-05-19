from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'home.html')

def inquire(request):
    return render(request, "inquire.html")