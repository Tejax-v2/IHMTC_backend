from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.method == "GET":
        return render(request, "loginsystem/home.html")

def signup(request):
    if request.method == "GET":
        return render(request, "loginsystem/signup.html")
    elif request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        print(email, pass1, pass2)
        return HttpResponse("Signup Successful")

def signin(request):
    if request.method == "GET":
        return render(request, "loginsystem/signin.html")
    elif request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)
        return HttpResponse("Signin Successful")

def forgot_password(request):
    if request.method == "GET":
        return render(request, "loginsystem/forgot-password.html")
    elif request.method == "POST":
        email = request.POST.get("email")
        print(email)
        return HttpResponse("Password reset link sent to your email") 

def reset_password(request):
    if request.method == "GET":
        return render(request, "loginsystem/reset-password.html")
    elif request.method == "POST":
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        print(pass1, pass2)
        return HttpResponse("Password reset successful")

def control_panel(request):
    if request.method == "GET":
        return render(request, "loginsystem/control-panel.html")
    elif request.method == "POST":
        email = request.POST.get("email")
        print(email)
        return HttpResponse("Control Panel")