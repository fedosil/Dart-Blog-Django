from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class Post_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm
    save_on_top = True
    list_display = ['id', 'title', 'slug', 'category', 'pinned_to', 'created_at', 'get_photo', 'views']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_editable = ['pinned_to']
    list_filter = ['category', 'tags']
    readonly_fields = ['views', 'created_at', 'get_photo']
    fields = ['title', 'slug', 'author', 'pinned_to', 'category', 'tags', 'content', 'photo', 'get_photo', 'views',
              'created_at']

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


class Category_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class Tag_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, Category_admin)
admin.site.register(Tag, Tag_admin)
admin.site.register(Post, Post_admin)
