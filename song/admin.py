from django.contrib import admin
from song.models import Singer, Song, Album


admin.site.register(Singer)
admin.site.register(Song)
admin.site.register(Album)
# Register your models here.
