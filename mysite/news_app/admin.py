from django.contrib import admin
from .models import Category, News, Comment


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ['name']}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'updated_at', 'is_published']
    list_editable = ['is_published']
    list_filter = ['category', 'created_at', 'is_published']
    search_fields = ['title']
    ordering = ['-created_at']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['news', 'username', 'content', 'created_at']
