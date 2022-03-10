from statistics import mode
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True)


class Post(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    text = models.TextField()
    likes_count = models.IntegerField(default=0, blank=True, null=True)

class Likes(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    comment_value = models.TextField()
