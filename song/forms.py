from django.forms import ModelForm
from django.core.exceptions import ValidationError
from song.models import Singer, Song, Album


class SingerForm(ModelForm):
    class Meta:
        model = Singer  # model to use in form
        # list of fields to be displayed
        fields = ['first_name', 'last_name']


class SongForm(ModelForm):
    class Meta:
        model = Song  # model to use in form
        # list of fields to be displayed
        fields = ['title', 'singer', 'album', 'date_published']

class AlbumForm(ModelForm):
    class Meta:
        model = Album  # model to use in form
        # list of fields to be displayed
        fields = ['name']