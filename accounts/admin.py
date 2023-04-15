from django.contrib import admin
from .models import Profile

# Register your models here.
app_name = 'accounts'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'date_of_birth')
