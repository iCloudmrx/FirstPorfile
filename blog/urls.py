from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', post_index, name='post_index'),
    path('contact/', post_contact, name='contact'),
    path('404/', post_contact, name='404'),
]
