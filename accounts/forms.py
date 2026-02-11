from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'phone', 'age', 'address',
            'education', 'experience', 'skills', 'position',
            'salary_expectation', 'about', 'password1', 'password2'
        ]

    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Этот ник уже занят. Выберите другой.")
        return username


class LoginForm(AuthenticationForm):
    captcha = CaptchaField()
