from django.contrib import admin

from blogs.models import Category, Blogger

admin.site.register(Category)
admin.site.register(Blogger)