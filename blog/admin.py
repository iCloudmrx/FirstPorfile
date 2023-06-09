from django.contrib import admin
from .models import *

# Register your models here.

app_name = 'blog'


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'publish', 'status']
    list_filter = ['title', 'category', 'publish', 'created']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    search_fields = ['title', 'publish', 'category']
    ordering = ['status', 'publish']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    list_filter = ['name', 'email']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_time', 'active']
    list_filter = ['active', 'created_time', 'user']
    search_fields = ['user', 'body']
    actions = ['disable_comments', 'activate_comments']

    def disable_comments(self, request, queryset):
        queryset.updated(active=False)

    def activate_comments(self, request, queryset):
        queryset.updated(active=True)
