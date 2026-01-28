from django.shortcuts import render
from blogs.models import Categories, Blog


def home(request):
    featured = Blog.objects.filter(is_featured=True, status="PUBLISHED")
    posts = Blog.objects.filter(is_featured=False, status="PUBLISHED")
    context = {"featured": featured, "posts": posts}
    return render(request, "home-blogs.html", context=context)
