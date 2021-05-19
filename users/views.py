from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse

from .models import User

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증 성공")
            login(request, user)
        else:
            print("인증 실패")
        return redirect(reverse("main_page:home"))

    else:
        return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect(reverse("main_page:home"))


def signup_view(request):

    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        address = request.POST["address"]

        user = User.objects.create_user(username, email, password)
        user.phone_number = phone_number
        user.address = address
        user.last_name = lastname
        user.first_name = firstname
        user.save()
        return redirect(reverse("users:login"))

    return render(request, "users/signup.html")