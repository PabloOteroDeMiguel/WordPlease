from django.contrib import admin

from posts.models import Post
from blogs.models import Category, Blogger

admin.site.register(Category)
admin.site.register(Blogger)
admin.site.register(Post)