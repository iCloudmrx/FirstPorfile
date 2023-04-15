from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from accounts.models import Profile
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

from django.contrib import messages


def signUpPage(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            Profile.objects.create(user=form)
            messages.success(request, 'Registration successful.')
            return redirect("blog:post_index")
        messages.error(
            request, 'Unsuccessful registration. Invalid information.')
    form = SignUpForm()
    return render(request, 'account/signup.html', {
        'form': form
    })


class SignUpView(CreateView):
    success_url = reverse_lazy('accounts:login')
    template_name = 'account/signup.html'
    form_class = UserCreationForm


def loginPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password'])
            (data)
            (user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("OK")
                else:
                    return HttpResponse("No active")
            else:
                return HttpResponse("Parolda xatolik bor")
        else:
            return HttpResponse("Mavjud emas")
    else:
        form = LoginForm()
        ('xatolik bor')
    return render(request, 'account/login.html', {
        'form': form
    })


def dashboard_view(request):
    user = request.user
    return render(request, 'pages/dashboard.html', {
        'user': user
    })


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("blog:post_index")


def user_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(
        instance=request.user.profile)
    return render(request, 'account/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
