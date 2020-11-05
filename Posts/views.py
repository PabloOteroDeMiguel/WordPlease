from django.shortcuts import render

from Posts.models import Post


def home(request):
     latest_posts = Post.objects.all().order_by("-created_at")
     context = {'Posts': latest_posts}
     return render(request, "home.html", context)