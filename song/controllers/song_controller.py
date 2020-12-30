from django.shortcuts import render
from song.models.song import Song
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from song.forms import SongForm
from django.contrib.auth.decorators import login_required
@login_required

def index(request):
    if request.method == 'POST':
        req = request.POST.dict()
        title = req['title']
        songs = Song.objects.filter(title__icontains=title)
    else:
        songs = Song.objects.all()
    data = {
        'songs': songs,
    }
    return render(request, 'song/songs.html', context=data)


def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('songs'))
    else:
        form = SongForm()

    context = {
        'form': form
    }
    return render(request, 'song/song_form.html', context=context)
