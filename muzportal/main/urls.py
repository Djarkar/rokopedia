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
    path('profile', Profile.as_view(), name='profile'),
    path('profile/updateavatar/<int:id_upd>', ChangeProfileImg.as_view(), name='updateavatar'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)