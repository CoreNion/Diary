from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomUserSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class AccountDeleteForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="パスワード")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not self.user.check_password(password):
            raise forms.ValidationError("パスワードが正しくありません。")
        return password