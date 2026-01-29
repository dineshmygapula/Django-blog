from django.shortcuts import render, get_object_or_404
from .models import Blog, Categories
from django.db.models import Q
from django.http import HttpResponse


# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(category_id=category_id, status="PUBLISHED")
    cate = Categories.objects.get(id=category_id)
    context = {
        "posts": posts,
        "cate": cate,
    }
    return render(request, "posts_by_category.html", context=context)


def blog(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status="PUBLISHED")
    return render(request, "blogs.html", {"single_blog": single_blog})


def search(request):
    keyword = request.GET.get("keyword")
    blog = Blog.objects.filter(
        Q(title__icontains=keyword)
        | Q(short_description__icontains=keyword)
        | Q(blog_body__icontains=keyword),
        status="PUBLISHED",
    )
    context = {"blog": blog, "keyword": keyword}
    return render(request, "search.html", context)
