from django.contrib import admin
from .models import *

# Register your models here.

app_name = 'blog'


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish', 'status']
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
