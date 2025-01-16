from django.shortcuts import render
from django.contrib.auth import views as auth_views, authenticate, login
from django.views.generic import CreateView, UpdateView

from django.urls import reverse_lazy
from django.http import HttpResponse

from .forms import CustomUserSignUpForm

class LoginView(auth_views.LoginView):
  template_name = "accounts/login.html"

class SignUpView(CreateView):
  form_class = CustomUserSignUpForm
  template_name = "accounts/signup.html"
  success_url = reverse_lazy("diary:home")

  def form_valid(self, form):
    response = super().form_valid(form)

    username = form.cleaned_data.get("username")
    password = form.cleaned_data.get("password1")
    user = authenticate(username=username, password=password)
    login(self.request, user)
    
    return response