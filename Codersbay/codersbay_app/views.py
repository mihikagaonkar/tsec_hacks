from sqlite3 import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import User
# Create your views here.

def login(request):
    return render(request, 'codersbay_app/auth.html')

def home(request):
    return render(request, 'codersbay_app/home.html')

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