from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, login
# Create your views here.


def signUpPage(request):
    form = SignUpForm(request.POST or None)
    if form.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse("Siz ro'yxatdan o'tdingiz")
    else:
        return render(request, 'account/signup.html', {
            'form': form
        })


def loginPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password'])
            print(data)
            print(user)
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
        print('xatolik bor')
    return render(request, 'account/login.html', {
        'form': form
    })


def dashboard_view(request):
    user = request.user
    return render(request, 'pages/dashboard.html', {
        'user': user
    })
