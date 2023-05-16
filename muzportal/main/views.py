from datetime import datetime
from typing import Any, Dict, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from django.views import generic
from django.urls import resolve, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin

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
        news = News_img.objects.order_by('-article__date').all()[:9]
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

    def get_queryset(self):
        return News_img.objects.order_by('-article__date').all()

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

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['songs'] = Songs.objects.filter(album__id=self.kwargs['id_album'])
        return context

class Profile(LoginRequiredMixin,generic.UpdateView):
    login_url = '/signin'
    redirect_field_name = ''
    model = User
    template_name = 'main/profile.html'
    form_class = ChangeNameProfile
    pk_url_kwarg = 'id_prof'
    context_object_name = 'user'

    def get_object(self):
        id_ = self.kwargs['id_prof']
        return get_object_or_404(User, id=id_)
    
    def get_success_url(self):
        return reverse('profile', args={self.kwargs['id_prof']})

class AllConcerts(generic.ListView):
    model = Concects_img
    template_name = 'main/concerts.html'
    context_object_name = 'concerts'

class AllPostsForum(LoginRequiredMixin,generic.ListView):
    login_url = '/signin'
    redirect_field_name = ''
    model = Posts
    template_name = 'main/allpostsforum.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Posts.objects.order_by('-post_date').all()

class AddPost(LoginRequiredMixin,generic.CreateView):
    login_url = '/signin'
    redirect_field_name = ''
    model = Posts
    template_name = 'main/addpost.html'
    context_object_name = 'post'
    form_class = AddPostForm

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('myposts')
    
class CurPost(LoginRequiredMixin,generic.CreateView):
    login_url = '/signin'
    redirect_field_name = ''
    model = Comments_forum
    template_name = 'main/curpost.html'
    context_object_name = ''
    pk_url_kwarg = 'id_post'
    form_class = CommentsForm

    def get_queryset(self):
        return Comments_forum.objects.filter(post__pk=self.kwargs['id_post'])
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['post'] = Posts.objects.get(id=self.kwargs['id_post'])
        context['com'] = Comments_forum.objects.filter(post__pk=self.kwargs['id_post']).order_by('post_date').all()
        context['count'] = Comments_forum.objects.filter(post__pk=self.kwargs['id_post']).count()
        return context
    
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.instance.post_id = self.kwargs['id_post']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('curpost', args={self.kwargs['id_post']})
    
class DeletePost(LoginRequiredMixin,generic.DeleteView):
    login_url = '/signin'
    redirect_field_name = ''
    model = Posts
    template_name = 'main/deletepost.html'
    pk_url_kwarg = 'id_post_delete'
    context_object_name = 'post'
    success_url = reverse_lazy('myposts')

class MyPosts(LoginRequiredMixin,generic.ListView):
    login_url = '/signin'
    redirect_field_name = ''
    model = Posts
    template_name = 'main/myposts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Posts.objects.filter(user__id=self.request.user.id).order_by('-post_date').all()
    
class CategoryPost(LoginRequiredMixin,generic.ListView):
    login_url = '/signin'
    redirect_field_name = ''
    model = Posts
    template_name = 'main/myposts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Posts.objects.filter(category__id=self.kwargs['id_cat']).order_by('-post_date').all()

class ForumRules(LoginRequiredMixin,generic.ListView):
    login_url = '/signin'
    redirect_field_name = ''
    model = User
    template_name = 'main/forumrules.html'




