from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "loginsystem/home.html")

def signup(request):
    return render(request, "loginsystem/signup.html")

def signin(request):
    return render(request, "loginsystem/signin.html")

def forgot_password(request):
    return render(request, "loginsystem/forgot-password.html")

def reset_password(request):
    return render(request, "loginsystem/reset-password.html")

def control_panel(request):
    return render(request, "loginsystem/control-panel.html")