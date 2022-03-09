from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True)
