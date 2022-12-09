from django.urls import path


from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', Posts_by_category.as_view(), name='category'),
    path('post/<str:slug>/', Single_post.as_view(), name='post'),
    path('tag/<str:slug>/', Posts_by_tag.as_view(), name='tag'),
    path('search/', Search.as_view(), name='search'),
]

