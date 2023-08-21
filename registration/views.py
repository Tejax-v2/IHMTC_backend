from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def participant_details(request):
    return render(request,"registration/participant-details.html")

def payment_details(request):
    return render(request,"payment-details.html")