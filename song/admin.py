from django.contrib import admin
from song.models import singer, song, album


admin.site.register(singer.Singer)
admin.site.register(song.Song)
admin.site.register(album.Album)
# Register your models here.
