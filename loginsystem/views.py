from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from IHMTC_backend import settings
from django.utils.safestring import mark_safe
from registration.models import Participant
import uuid
from IHMTC_backend.utilities import send_reset_link

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
        return redirect("home")

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
        response = redirect("home")
        response.set_cookie('email', email, max_age=settings.SESSION_COOKIE_AGE)
        return response

def forgot_password(request):
    if request.method == "GET":
        return render(request, "loginsystem/forgot-password.html")
    elif request.method == "POST":
        email = request.POST.get("email")
        token = uuid.uuid4()
        user = None
        try:
            user = User.objects.get(username=email)
        except:
            print("Some error occured")
        send_reset_link(email, token)
        participant = Participant.objects.get(email=user)
        participant.forgot_pass_token = token
        participant.save()
        print(email)
        return redirect("home")

def reset_password(request,token):
    if request.method == "GET":
        return render(request, "loginsystem/reset-password.html")
    elif request.method == "POST":
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        errors={}
        if not pass1 or not pass2:
            errors["missingInputs"]="Please fill out all fields"
        elif pass1 != pass2:
            errors["passwordMismatch"]="Passwords not matching"
        if(not errors):
            try:
                participant = Participant.objects.get(forgot_pass_token=token)
                user = participant.email
                user.set_password(pass1)
                user.save()
            except:
                return HttpResponse("Password reset failed")
        return redirect("home")

def control_panel(request):
    if request.method == "GET":
        return render(request, "loginsystem/control-panel.html")
    elif request.method == "POST":
        email = request.POST.get("email")
        print(email)
        return HttpResponse("Control Panel")
    
def signout(request):
    if request.method == "GET":
        logout(request)  
        response = redirect('home')  
        try:
            response.delete_cookie('email')
        except:
            pass
        return response