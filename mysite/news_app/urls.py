from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsHome.as_view(), name='index'),
    path('category/<slug:categories_name>', views.NewsCategory.as_view(), name='categories'),
    path('post/<slug:post_name>', views.ShowPost.as_view(), name='post'),
    path('search', views.NewsSearch.as_view(), name='news-search'),
    path('create', views.NewsCreateView.as_view(), name='create-post'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('logout', views.logout_user, name='logout'),
]