from django.contrib import admin
from .models import *

class Albums_imgAdmin(admin.ModelAdmin):
    list_display = ('id','album')
    list_display_links = ('id', 'album')
    search_fields = ('album',)

admin.site.register(Albums_img, Albums_imgAdmin)

admin.site.register(Albums)

admin.site.register(Genres)

admin.site.register(Artist_img)

admin.site.register(Artists)

admin.site.register(Songs)

class Concerts_imgAdmin(admin.ModelAdmin):
    list_display = ('concert',)
    list_display_links = ('concert',)
    search_fields = ('concert',)

admin.site.register(Concects_img, Concerts_imgAdmin)

admin.site.register(Concerts)

admin.site.register(Comments_news)

admin.site.register(Categories_news)

admin.site.register(News_img)

admin.site.register(Articles)

admin.site.register(User_img)