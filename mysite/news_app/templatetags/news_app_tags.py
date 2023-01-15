from django import template
from news_app.models import Category


register = template.Library()


@register.inclusion_tag('news_app/list_categories.html')
def show_categories(cat_selected=None):
    cats = Category.objects.all()
    return {
        'cats': cats,
        'cat_selected': cat_selected
    }