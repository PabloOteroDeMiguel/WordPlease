from django.contrib.auth.models import User
from django.db import models


class Blogger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    profile_picture = models.URLField()
    birthday = models.DateField()

    def __str__(self):
        return self.user


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
