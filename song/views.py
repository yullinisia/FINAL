from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from song.models import Song, Singer, Album
from song.forms import SingerForm, SongForm, AlbumForm


def record(request):
    # get all info here including singers, songs, and albums
    num_songs = Song.objects.all().count()
    num_singers = Singer.objects.all().count()
    num_albums = Album.objects.all().count()
    context = {
        'num_songs': num_songs,
        'num_singers': num_singers,
        'num_albums': num_albums,
    }
    return render(request, 'record.html', context=context)


def list_singers(request):
    singers = Singer.objects.all()
    context = {
        'singers': singers,
    }
    return render(request, 'singers.html', context=context)


def list_songs(request):
    songs = Song.objects.all()
    context = {
        'songs': songs,
    }
    return render(request, 'songs.html', context=context)


def list_albums(request):
    albums = Album.objects.all()
    context = {
        'albums': albums,
    }
    return render(request, 'albums.html', context=context)

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('albums'))
    else:
        form = AlbumForm()

    context = {
        'form': form
    }
    return render(request, 'album_form.html', context=context)

def edit_album(request, album_id):
    if request.method == 'POST':
        album = Album.objects.get(pk=album_id)
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('albums'))
    else:
        album = Album.objects.get(pk=album_id)
        fields = model_to_dict(album)
        form = AlbumForm(initial=fields, instance=album)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'album_form.html', context=context)

def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    if request.method == 'POST':
        album.delete()
        return HttpResponseRedirect(reverse('albums'))
    context = {
        'album': album
    }
    return render(request, 'album_delete_form.html', context=context)


def add_singer(request):
    if request.method == 'POST':
        form = SingerForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('singers'))
    else:
        form = SingerForm()

    context = {
        'form': form
    }
    return render(request, 'singer_form.html', context=context)


def edit_singer(request, singer_id):
    if request.method == 'POST':
        singer = Singer.objects.get(pk=singer_id)
        form = SingerForm(request.POST, instance=singer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('singers'))
    else:
        singer = Singer.objects.get(pk=singer_id)
        fields = model_to_dict(singer)
        form = SingerForm(initial=fields, instance=singer)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'singer_form.html', context=context)


def delete_singer(request, singer_id):
    singer = Singer.objects.get(pk=singer_id)
    if request.method == 'POST':
        singer.delete()
        return HttpResponseRedirect(reverse('singers'))
    context = {
        'singer': singer
    }
    return render(request, 'singer_delete_form.html', context=context)


def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
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
