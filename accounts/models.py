from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="users/", height_field=None,
                              width_field=None, max_length=None, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username
