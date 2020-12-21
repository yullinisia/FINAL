from django.urls import path
from . import views
from song.controllers import song_controller, album_controller, singer_controller

urlpatterns = [
    path('', views.record, name='record'),
    path('singers/', singer_controller.index, name='singers'),
    path('singer/add', views.add_singer, name='add_singer'),
    path('singer/edit/<int:singer_id>', views.edit_singer, name='edit_singer'),
    path('singer/delete/<int:singer_id>', views.delete_singer, name='delete_singer'),
    path('songs/', views.list_songs, name='songs'),
    path('song/add', views.add_song, name='add_song'),
    path('song/edit/<int:song_id>', views.edit_song, name='edit_song'),
    path('song/delete/<int:song_id>', views.delete_song, name='delete_song'),
    path('albums/', album_controller.index, name='albums'),
    path('album/add', views.add_album, name='add_album'),
    path('album/edit/<int:album_id>', views.edit_album, name='edit_album'),
    path('album/delete/<int:album_id>', views.delete_album, name='delete_album'),
]