from django.contrib import admin
from song.models.singer import Singer
from song.models.song import Song
from song.models.album import Album
from song.models.genre import Genre
from song.models.producer import Producer

admin.site.register(Singer)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Producer)
# Register your models here.
