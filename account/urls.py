from django.urls import path
from account.views import register,login,reset_password_email,reset_password,change_password

urlpatterns = [
    path('account/register/',register, name='register'),
    path('account/login/',login, name='login'),
    path('account/reset-password-email/',reset_password_email, name='reset-password-email'),
    path('account/reset-password/',reset_password, name="reset-password"),
    path('account/change-password/',change_password, name="change_password"),
]
