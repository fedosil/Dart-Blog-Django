from django import template
from blog.models import Category, Post, Tag
from django.core.cache import cache

register = template.Library()

@register.inclusion_tag('blog/tags/sitebar_popular.html')
def show_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}

@register.inclusion_tag('blog/tags/sitebar_tags.html')
def show_tags():
    tags = Tag.objects.all()
    return {'tags': tags}