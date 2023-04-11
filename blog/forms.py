from django import forms
from .models import Contact, Customer


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class RegisterForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['email', 'password']
