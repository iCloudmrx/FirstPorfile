from django.db import models

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
