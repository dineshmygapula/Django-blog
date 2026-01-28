from django.shortcuts import render
from .models import Blog, Categories


# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(category_id=category_id, status="PUBLISHED")
    cate = Categories.objects.get(id=category_id)
    context = {
        "posts": posts,
        "cate": cate,
    }
    return render(request, "posts_by_category.html", context=context)
