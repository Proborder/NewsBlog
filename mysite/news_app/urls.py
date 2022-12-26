from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:categories_name>', views.show_category, name='categories'),
    path('post/<slug:post_name>', views.show_post, name='post')
]