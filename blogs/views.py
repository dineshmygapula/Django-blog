from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Categories
from django.db.models import Q
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


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


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("register")
    form = RegistrationForm()
    return render(request, "register.html", context={"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect("home")

    form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "login.html", context)


def logout(request):
    auth.logout(request)
    return redirect("home")
