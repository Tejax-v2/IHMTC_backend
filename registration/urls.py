from django.urls import path
from . import views

urlpatterns = [
    path('participant-details/', views.participant_details, name='participant-details'),
    path('payment-details/', views.payment_details, name='payment-details'),
]