from django.urls import path

from .views import edit_user_profile, log_out, register, loginـuser, user_account_main_page

urlpatterns = [
    path('login', loginـuser),
    path('register', register),
    path('log-out', log_out),
    path('user', user_account_main_page),
    path('user/edit', edit_user_profile)
]