from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout

from .models import Category, News, Comment
from .forms import CommentForm, NewsForm, RegisterUserForm, LoginUserForm
from .utils import DataMixin


class NewsHomeView(DataMixin, ListView):
    model = News
    template_name = 'news_app/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return context | c_def

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsCategoryView(DataMixin, ListView):
    model = News
    template_name = 'news_app/show_category.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['categories_name'])
        c_def = self.get_user_context(cat_selected=self.kwargs['categories_name'])
        return context | c_def

    def get_queryset(self):
        return News.objects.filter(category__slug=self.kwargs['categories_name'], is_published=True).select_related('category')


class ShowPostView(ModelFormMixin, DetailView):
    model = News
    form_class = CommentForm
    template_name = 'news_app/show_post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(news__slug=self.kwargs['post_name'])
        context['comments'] = Comment.objects.filter(news__slug=self.kwargs['post_name']).select_related('username')
        context['form'] = CommentForm(initial={'username': self.request.user, 'news': self.object})
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = self.get_object()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('post', kwargs={'post_name': self.kwargs['post_name']})


class NewsSearchView(DataMixin, ListView):
    model = News
    template_name = 'news_app/index.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return context | c_def

    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(title__icontains=query, is_published=True).select_related('category')


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'news_app.change_post'
    model = News
    template_name = 'news_app/create_post.html'
    slug_url_kwarg = 'post_name'
    form_class = NewsForm


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'news_app.delete_post'
    model = News
    slug_url_kwarg = 'post_name'
    success_url = reverse_lazy('index')


class NewsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'news_app.add_news'
    form_class = NewsForm
    template_name = 'news_app/create_post.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'news_app/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'news_app/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')
