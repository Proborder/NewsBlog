from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsHomeView.as_view(), name='index'),
    path('category/<slug:categories_name>/', views.NewsCategoryView.as_view(), name='categories'),
    path('post/<slug:post_name>/', views.ShowPostView.as_view(), name='post'),
    path('search/', views.NewsSearchView.as_view(), name='news-search'),
    path('create/', views.NewsCreateView.as_view(), name='create-post'),
    path('<slug:post_name>/update/', views.NewsUpdateView.as_view(), name='update-post'),
    path('<slug:post_name>/delete/', views.NewsDeleteView.as_view(), name='delete-post'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
]
