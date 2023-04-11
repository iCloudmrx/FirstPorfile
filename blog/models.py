from django import forms
from django.db import models
from django.urls import reverse
from django.utils import timezone
from .managers import PublishedManager
# Create your models here.

# class PublishedManager(models.Manager):
#     get


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'DRAFT'
        Published = 'PB', 'PUBLISHED'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft)

    objects = models.Manager()  # The default manger
    published = PublishedManager()  # our custom manager

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug])


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email


class Customer(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True, blank=False, max_length=254)
    password = models.CharField(max_length=16)
    c_password = models.CharField(max_length=16)

    def __str__(self):
        return self.username
