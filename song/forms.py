from django.forms import ModelForm
from django.core.exceptions import ValidationError
from song.models import Singer, Song, Album, Genre, Producer


class SingerForm(ModelForm):
    class Meta:
        model = Singer  # model to use in form
        # list of fields to be displayed
        fields = ['first_name', 'last_name']


class SongForm(ModelForm):
    class Meta:
        model = Song  # model to use in form
        # list of fields to be displayed
        fields = ['title', 'singer', 'album', 'genre', 'producer', 'date_published']

class AlbumForm(ModelForm):
    class Meta:
        model = Album  # model to use in form
        # list of fields to be displayed
        fields = ['name']

class GenreForm(ModelForm):
    class Meta:
        model = Genre  # model to use in form
        # list of fields to be displayed
        fields = ['name', 'description']

class ProducerForm(ModelForm):
    class Meta:
        model = Producer  # model to use in form
        # list of fields to be displayed
        fields = ['name']