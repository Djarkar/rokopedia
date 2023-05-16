from datetime import datetime
from typing import Any
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

class ChangeNameProfile(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='Введите ваш имя', widget=forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder': 'Введите новое имя'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name',)

class AddPostForm(forms.ModelForm):
    topic = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control forms_django', 'placeholder' : 'Название темы', 'style': 'max-width: 500px; width: 80%; margin-left: auto; margin-right: auto;', 'aria-label': "Example text with button addon", 'aria-describedby':"button-addon1"}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control", 'placeholder':"Описание темы", 'id':"exampleFormControlTextarea1", 'rows':"5"}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class':"form-select", 'aria-label':"Default select example"}), queryset=Categories_post.objects.all())
    img = forms.ImageField(widget=forms.FileInput(attrs={'class':"form-control", 'id':"formFile"}))
    class Meta:
        model = Posts
        fields= ('topic','body', 'category', 'img', )

class CommentsForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':'3', 'cols':'50', 'class':'form-control form-control-lg', 'placeholder':'Комментарий'}))

    class Meta:
        model = Comments_forum
        fields = ('body',)