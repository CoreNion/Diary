from django.urls import include, path
from django.contrib.auth.views import LogoutView

from . import views

app_name = "accounts"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("setting", views.SettingView.as_view(), name="setting"),
    path("password_change", views.PasswordChangeView.as_view(), name="password_change"),
    path("delete", views.AccountDeleteView.as_view(), name="delete"),
]