from django.core.paginator import Paginator
from django.shortcuts import render
from song.models.singer import Singer
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from song.forms import SingerForm
from django.contrib.auth.decorators import login_required
@login_required


def index(request):
    singers = Singer.objects.all()
    paginator = Paginator(singers, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'page_obj': page_obj
    }
    return render(request, 'singer/singers.html', context=data)

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
    return render(request, 'singer/singer_form.html', context=context)

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
    return render(request, 'singer/singer_form.html', context=context)


def delete_singer(request, singer_id):
    singer = Singer.objects.get(pk=singer_id)
    if request.method == 'POST':
        singer.delete()
        return HttpResponseRedirect(reverse('singers'))
    context = {
        'singer': singer
    }
    return render(request, 'singer/singer_delete_form.html', context=context)
