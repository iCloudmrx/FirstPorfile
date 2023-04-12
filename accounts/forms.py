from django import forms
from .models import Customer


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
