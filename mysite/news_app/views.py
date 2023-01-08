from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from .models import Category, News
from .forms import NewsForm


class NewsHome(ListView):
    model = News
    template_name = 'news_app/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsCategory(ListView):
    model = News
    template_name = 'news_app/show_category.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['categories_name'])
        context['categories'] = Category.objects.all()
        context['cat_selected'] = self.kwargs['categories_name']
        return context

    def get_queryset(self):
        return News.objects.filter(category__slug=self.kwargs['categories_name'], is_published=True)


class ShowPost(DetailView):
    model = News
    template_name = 'news_app/show_post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class NewsCreateView(CreateView):
    form_class = NewsForm
    template_name = "news_app/create_post.html"
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
