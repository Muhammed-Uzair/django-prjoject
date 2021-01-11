from django.contrib import admin
from .models import Post, Category
from django.db import models
# Register your models here.
from tinymce.widgets import TinyMCE


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author')
    prepopulated_fields = {
        'slug': ('title',),
    }
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


# @admin.register(Comment)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('post', 'name', 'email', 'publish', 'status')
#     list_filter = ('status', 'publish')
#     search_fields = ('name', 'email', 'content')


admin.site.register(Category)
