from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def participant_details(request):
    return HttpResponse("Participant Details")

def payment_details(request):
    return HttpResponse("Payment Details")