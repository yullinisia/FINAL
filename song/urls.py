from django.urls import path
from song.controllers import song_controller, album_controller, singer_controller, record_controller, registration_controller

urlpatterns = [
    path('', record_controller.record, name='record'),
    path('singers/', singer_controller.index, name='singers'),
    path('singer/add', singer_controller.add_singer, name='add_singer'),
    path('singer/edit/<int:singer_id>', singer_controller.edit_singer, name='edit_singer'),
    path('singer/delete/<int:singer_id>', singer_controller.delete_singer, name='delete_singer'),
    path('songs/', song_controller.index, name='songs'),
    path('song/add', song_controller.add_song, name='add_song'),
    path('song/edit/<int:song_id>', song_controller.edit_song, name='edit_song'),
    path('song/delete/<int:song_id>', song_controller.delete_song, name='delete_song'),
    path('albums/', album_controller.index, name='albums'),
    path('album/add', album_controller.add_album, name='add_album'),
    path('album/edit/<int:album_id>', album_controller.edit_album, name='edit_album'),
    path('album/delete/<int:album_id>', album_controller.delete_album, name='delete_album'),
    path('register', registration_controller.index, name='register'),
]