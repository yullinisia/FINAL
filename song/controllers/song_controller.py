from django.shortcuts import render
from song.models.song import Song
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from song.forms import SongForm


def index(request):
    if request.method == 'POST':
        req = request.POST.dict()
        name = req['name']
        songs = Song.objects.filter(name__contains=name)
    else:
        songs = Song.objects.all()
    data = {
        'songs': songs,
    }
    return render(request, 'songs.html', context=data)


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
    return render(request, 'song_form.html', context=context)


def edit_song(request, song_id):
    if request.method == 'POST':
        song = Song.objects.get(pk=song_id)
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('songs'))
    else:
        song = Song.objects.get(pk=song_id)
        fields = model_to_dict(song)
        form = SongForm(initial=fields, instance=song)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'song_form.html', context=context)


def delete_song(request, song_id):
    song = Song.objects.get(pk=song_id)
    if request.method == 'POST':
        song.delete()
        return HttpResponseRedirect(reverse('songs'))
    context = {
        'song': song,
    }
    return render(request, 'song_delete_form.html', context=context)

