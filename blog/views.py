from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, News

# Create your views here.


def home(request):
    all_news = News.objects.all()
    all_blogs = Blog.objects.filter().order_by('-date_added')
    context = {
        'news': all_news,
        'blogs': all_blogs
    }
    return render(request, "blog/index.html", context=context)


def blog(request):
    return render(request, "blog/blog.html")


def blog_details(request):
    return render(request, "blog/blog-details.html")
