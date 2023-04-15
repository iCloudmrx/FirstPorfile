from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    fullname = models.CharField(max_length=230)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True, blank=False, max_length=254)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    c_password = models.CharField(max_length=16)

    def __str__(self):
        return self.fullname


class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="user/", height_field=None,
                              width_field=None, max_length=None, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username
