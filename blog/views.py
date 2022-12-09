from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import F

from .models import Post, Category, Tag

class Search(ListView):
    model = Post
    template_name = 'blog/search_post_list.html'
    paginate_by = 4
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поиск'
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context

class Single_post(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class Home(ListView):
    model = Post
    template_name = 'blog/home_post_list.html'
    paginate_by = 4
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        context['posts_pinned_to'] = self.model.objects.filter(pinned_to=True)
        return context


class Posts_by_category(Home):
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

class Posts_by_tag(Home):
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context
