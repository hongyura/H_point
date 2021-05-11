from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
# Create your views here.

def login_view(request):
    if request.method == "post":
        username = request.post["username"]
        password = request.post["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증 성공")
            login(request, user)
        else:
            print("인증 실패")
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("user:login")


def signup_view(request):

    if request.method == "post":
        username = request.post["username"]
        password = request.post["password"]
        email = request.post["email"]
        phone_number = request.post["phone_number"]
        firstname = request.post["firstname"]
        lastname = request.post["lastname"]

        user = User.objects.create_user(username, email, password)
        user.phone_number = phone_number
        user.last_name = lastname
        user.first_name = firstname
        user.save()

        return redirect("user:login")

    return render(request, "users/signup.html")