from sqlite3 import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth import login as authenticate_login

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


from .models import Person, Post, User
# Create your views here.

def login(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            authenticate_login(request, user)

            return redirect("home")
        else:
            return render(request, "codersbay_app/auth.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, 'codersbay_app/auth.html')

def home(request):
    user = request.user
    person = Person.objects.get(user=user)
    posts = Post.objects.filter(user=person)
    context = {'posts': posts}
    print(posts)
    return render(request, 'codersbay_app/home.html', context)

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
        except IntegrityError:  
            return render(request, 'codersbay_app/auth.html', {
                "message": "Username already taken."
            })
        return HttpResponseRedirect(reverse_lazy("home"))
    else:
        return render(request, 'codersbay_app/auth.html')

def like_post(request, id):
    user = request.user
    liked_post = Post.objects.get(pk=id)
    print(user)
    print(liked_post)
    return HttpResponse('Liked')

def complete_profile(request):
    return render(request, 'codersbay_app/complete_profile.html')

def complete_tech(request):
    return render(request, 'codersbay_app/complete_tech.html')