from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="login"), 
    path('home', views.home, name="home")
]
