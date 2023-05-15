from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import *
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from .models import *

class SignUp(generic.CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('main')
    template_name = 'main/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class SignIn(LoginView):
    model = User
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('main')
    
def logout_user(request):
    logout(request)
    return redirect('main')

class Main(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'data'

    def get_queryset(self):
        concerts = Concects_img.objects.all()
        news = News_img.objects.all()[:9]
        return {'concerts': concerts, 'news': news}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_queryset()
        context.update(data)
        return context


class AllNews(generic.ListView):
    model = News_img
    template_name = 'main/allnews.html'
    context_object_name = 'news'

class CurrentNews(generic.DetailView):
    model = News_img
    template_name = 'main/currentnews.html'
    context_object_name = 'cnews'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['randnews'] = News_img.objects.order_by('?').all().exclude(id=self.kwargs['id'])[:6]
        return context
    
class AllArtists(generic.ListView):
    model = Artist_img
    template_name = 'main/artists.html'
    context_object_name = 'artists'

class CurArtist(generic.DetailView):
    model = Artist_img
    template_name = 'main/currentart.html'
    context_object_name = 'curart'
    pk_url_kwarg = 'id_art'

    def get_queryset(self):
        return Artist_img.objects.filter(id=self.kwargs['id_art'])

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['albums'] = Albums_img.objects.filter(album__artist__id=self.kwargs['id_art'])
        return context

class Album(generic.DetailView):
    model = Albums_img
    template_name = 'main/album.html'
    context_object_name = 'album'
    pk_url_kwarg = 'id_album'

class Profile(generic.ListView):
    model = User
    template_name = 'main/profile.html'
    context_object_name = 'user'

    def get_queryset(self):
        return User.objects.get(username=self.request.user)
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        try:
            context['img'] = User_img.objects.filter(user__id = self.request.user.id).order_by('id').last()
        except User_img.DoesNotExist:
            context['img'] = User_img.objects.filter(user__id = self.request.user.id)
        return context

class ChangeProfileImg(generic.CreateView):
    model = User_img
    template_name = 'main/change.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id_upd'
    context_object_name = 'image'
    fields = ['img']
    
    def form_valid(self, form):
        img = form.save(commit=False)
        img.user = self.request.user
        img.save()
        return HttpResponseRedirect(reverse_lazy('profile'))

    def get_queryset(self):
        return User_img.objects.get(user__id=self.request.user.id)




