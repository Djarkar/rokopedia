from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Введите ваше логин', widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    first_name = forms.CharField(max_length=30, label='Введите ваш имя', widget=forms.TextInput(attrs={'placeholder': 'ФИО'}))
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'pass-key'}))
    password2 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'class': 'pass-key-repeat'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'password1', 'password2')

class CreateImageProfileForm(forms.ModelForm):
    image = forms.ImageField(label='Добавьте изображение', required=True)

    class Meta:
        model = News_img
        fields = ('img',)
