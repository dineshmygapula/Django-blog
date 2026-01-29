from .models import Categories, SocialLink


def get_categories(request):
    categories = Categories.objects.all()
    return {"categories": categories}


def get_social_links(request):
    link = SocialLink.objects.all()
    return dict(link=link)
