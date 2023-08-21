from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from IHMTC_backend import settings
from django.utils.safestring import mark_safe

# Create your views here.

def home(request):
    if request.method == "GET":
        if request.COOKIES.get("email"):
            navbtns = '<button class="btn btn-outline-primary me-2">'+request.COOKIES.get("email")+'</button><a href="/signout"><button class="btn btn-primary">Logout</button></a>'
        else:
            navbtns = '<a href="/signup"><button class="btn btn-outline-primary me-2">Sign Up</button></a><a href="/signin"><button class="btn btn-primary">Sign In</button></a>'
        navbtns = mark_safe(navbtns)
        return render(request, "loginsystem/home.html", {"navbtns":navbtns})

def signup(request):
    if request.method == "GET":
        return render(request, "loginsystem/signup.html")
    elif request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        print(email, pass1, pass2)
        user = None
        errors = {}
        if(User.objects.filter(email=email).exists()):
            errors['emailExist']="There is already an account with this email. Please try to login"
        if(pass1 and pass2 and (pass1 != pass2)):
            errors['passwordMismatch']="Passwords not matching"
        if(not email or not pass1 or not pass2):
            errors['missingInputs']="Please fill out all fields"
        if(not errors):
            user = User.objects.create_user(username=email, email=email, password=pass1)
        else:
            outputString = "<ul>"
            for value in errors:
                outputString+="<li>"+value+"</li>"
            outputString+="</ul>"
            return HttpResponse(outputString)
        user.save()
        return HttpResponse("Signup Successful")

def signin(request):
    if request.method == "GET":
        return render(request, "loginsystem/signin.html")
    elif request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        errors = {}
        if(not email or not password):
            errors['missingInputs']="Please fill out all fields"
        elif(not User.objects.filter(email=email).exists()):
            errors['emailNotExist']="There is no account for this email. Please Sign up first"
        if(not errors):
            user = authenticate(username=email,password=password)
            if(user):
                request.session.set_expiry(settings.SESSION_COOKIE_AGE)
                login(request, user)
            else:
                return()
        else:
            outputString = "<ul>"
            for value in errors:
                outputString+="<li>"+value+"</li>"
            outputString+="</ul>"
            return HttpResponse(outputString)
        print(user)
        response = HttpResponse("Signin Successful")
        response.set_cookie('email', email, max_age=settings.SESSION_COOKIE_AGE)
        return response

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
    
def signout(request):
    if request.method == "GET":
        logout(request)  # This will delete the user's session
        response = redirect('home')  # Replace 'home' with the URL name of your home screen
        try:
            response.delete_cookie('email')  # Delete any specific cookies if needed
        except:
            pass
        return response