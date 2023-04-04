from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    models = Contact
    fields = '__all__'
