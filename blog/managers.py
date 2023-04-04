from django.db import models
from .models import *


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
