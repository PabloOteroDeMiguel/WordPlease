from django.db import models
from blogs.models import Category

class Post(models.Model):

    title = models.CharField(max_length=30)
    text = models.CharField(max_length=140)
    media = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)