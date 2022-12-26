from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, News


# Create your views here.
def index(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context = {
        'title': 'Главная страница',
        'categories': categories,
        'news': news,
    }
    return render(request, 'news_app/index.html', context=context)