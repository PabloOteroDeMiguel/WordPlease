from django.contrib.auth.models import User
from django.db import models

class blogger(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    profile_picture = models.URLField()
    birthday = models.DateField()

    created_at = models.DateTimeField(auto_now=True)