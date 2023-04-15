from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', "password")

    # def clean_password2(self):
    #     data = self.cleaned_data
    #     if data['password1'] != data['password2']:
    #         raise forms.ValidationError("Parol bir xil emas")
    #     return data['password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['date_of_birth', 'photo']
