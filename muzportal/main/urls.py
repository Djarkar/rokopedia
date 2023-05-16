from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('signup', SignUp.as_view(), name='signup'),
    path('signin', SignIn.as_view(), name='signin'),
    path('logout', logout_user, name='logout'),
    path('news', AllNews.as_view(), name='news'),
    path('news/<int:id>', CurrentNews.as_view(), name='currentnews'),
    path('artists', AllArtists.as_view(), name='artists'),
    path('artists/<int:id_art>', CurArtist.as_view(), name='currentartist'),
    path('album/<int:id_album>', Album.as_view(), name='album'),
    path('profile/<int:id_prof>', Profile.as_view(), name='profile'),
    path('concerts', AllConcerts.as_view(), name='concerts'),
    path('forum/', AllPostsForum.as_view(), name='forum'),
    path('forum/addpost', AddPost.as_view(), name='addpost'),
    path('forum/posts/<int:id_post>', CurPost.as_view(), name='curpost'),
    path('forum/deletepost/<int:id_post_delete>', DeletePost.as_view(), name='deletepost'),
    path('forum/myposts', MyPosts.as_view(), name='myposts'),
    path('forum/category/<int:id_cat>', CategoryPost.as_view(), name='cat_post'),
    path('forum/rules', ForumRules.as_view(), name='forumrules')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)