from django.urls import path, reverse_lazy
from .views import *
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView)

app_name = 'accounts'
urlpatterns = [
    path('register/', signUpPage, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(success_url=reverse_lazy(
        'accounts:password_reset_done')), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('profile/', dashboard_view, name='dashboard'),
]
