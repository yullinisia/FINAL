from django.shortcuts import render
from song.models.producer import Producer
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from song.forms import ProducerForm
from django.contrib.auth.decorators import login_required
@login_required

def index(request):
    if request.method == 'POST':
        req = request.POST.dict()
        name = req['name']
        producers = Producer.objects.filter(name__icontains=name)
    else:
        producers = Producer.objects.all()
    data = {
        'producers': producers,
    }
    return render(request, 'producer/producers.html', context=data)

def add_producer(request):
    if request.method == 'POST':
        form = ProducerForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('producers'))
    else:
        form = ProducerForm()

    context = {
        'form': form
    }
    return render(request, 'producer/producer_form.html', context=context)