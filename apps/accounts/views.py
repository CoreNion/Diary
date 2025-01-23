from django.shortcuts import render
from django.contrib.auth import views as auth_views, authenticate, login
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import HttpResponse

from .forms import AccountDeleteForm, CustomUserSignUpForm
from .models import CustomUser

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
  
class SettingView(LoginRequiredMixin, UpdateView):
  model = CustomUser
  fields = {"username"}
  template_name = "accounts/setting.html"
  success_url = reverse_lazy("diary:setting")

  def get_object(self):
    return self.request.user
  
  def form_valid(self, form):
    response = super().form_valid(form)
    self.request.user.username = form.cleaned_data.get("username")
    self.request.user.save()
    return response
  
class PasswordChangeView(auth_views.PasswordChangeView):
  template_name = "accounts/password_change.html"
  success_url = reverse_lazy("diary:setting")

class AccountDeleteView(LoginRequiredMixin, FormView):
    template_name = "accounts/delete.html"
    form_class = AccountDeleteForm
    success_url = reverse_lazy("diary:home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        # アカウントを削除
        self.request.user.delete()
        return super().form_valid(form)