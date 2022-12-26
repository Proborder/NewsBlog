from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, News


# Create your views here.
def index(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, 'news_app/index.html', context=context)


def show_category(request, categories_name):
    categories = Category.objects.all()
    category = Category.objects.get(slug=categories_name)
    news = News.objects.filter(category__slug=categories_name)
    context = {
        'category': category,
        'categories': categories,
        'news': news,
        'cat_selected': categories_name,
    }
    return render(request, 'news_app/show_category.html', context=context)


def show_post(request, post_name):
    categories = Category.objects.all()
    post = News.objects.get(slug=post_name)
    context = {
        'categories': categories,
        'post': post
    }
    return render(request, 'news_app/show_post.html', context=context)