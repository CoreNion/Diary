from django.shortcuts import render
from django.contrib.auth import views as auth_views

from django.http import HttpResponse

class LoginView(auth_views.LoginView):
  template_name = "accounts/login.html"