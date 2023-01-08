from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsHome.as_view(), name='index'),
    path('category/<slug:categories_name>', views.NewsCategory.as_view(), name='categories'),
    path('post/<slug:post_name>', views.ShowPost.as_view(), name='post'),
    path('create', views.NewsCreateView.as_view(), name='create-post'),
]