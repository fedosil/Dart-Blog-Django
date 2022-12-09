from django import template
from blog.models import Category
from django.core.cache import cache

register = template.Library()

@register.inclusion_tag('blog/tags/menu.html')
def show_menu(menu_class='menu'):
    categories = cache.get_or_set('categories', Category.objects.all(), 5)
    return {'categories': categories, 'menu_class': menu_class}