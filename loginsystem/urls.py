from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('forgot-password/',views.forgot_password, name='forgot-password'),
    path('reset-password/',views.reset_password, name='reset-password'),
    path('control-panel/',views.control_panel, name='control-panel'),
]