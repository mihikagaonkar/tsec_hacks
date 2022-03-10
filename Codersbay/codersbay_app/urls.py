from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"), 
    path('home', views.home, name="home"),
    path('like_post/<int:id>', views.like_post, name="like_post"),
    path('complete_profile', views.complete_profile, name="complete_profile"),
    path('complete_tech', views.complete_tech, name="complete_tech"),
]
