from django.shortcuts import render

from Posts.models import Post


def home(request):
     latest_posts = Post.objects.all().order_by("-created_at")
     context = {'Posts': latest_posts}
     return render(request, "home.html", context)

def post_detail(request, pk):
    possible_post = Post.objects.filter(pk=pk).select_related("category")
    if len(possible_post) == 0:
        # pelicula no existe
        return render(request, "404.html", status=404)
    else:
        post = possible_post[0]
        context = {'post': Post}
        return render(request, "post_detail.html", context)
