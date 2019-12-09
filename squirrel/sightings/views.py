from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.db.models import Count, Q
from django.contrib import messages

from .models import Squirrel
from .form import SquirrelForm

def index(request):
    return render(request, 'sightings/index.html')

def sightings(request):
    squirrels = Squirrel.objects.all()
    return render(request, 'sightings/sightings.html', {'squirrels':squirrels})

def add(request):
    if request.method == "POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New sighting of squirrel is added successfully.")
            return render(request, 'sightings/add.html',{'form':form})
        else:
            context = {'form': form,
                        'error': "The sighting of squirrel cannot be added. Please check if the input values are valid."}
            return render(request,'sightings/add.html', context)
    else:
        form = SquirrelForm()
    return render(request, 'sightings/add.html', {'form': form})


def detail(request, unique_squirrel_id):
    squirrel = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    if request.method == "POST":
        form = SquirrelForm(request.POST,instance=squirrel)
        if form.is_valid():
            form.save()
            messages.success(request, "New sighting of squirrel is updated successfully.")
            return redirect(f'/sightings/{unique_squirrel_id}')
    else:
        form = SquirrelForm(instance=squirrel)
    context = {
        'form': form,
    }
    return render(request, 'sightings/detail.html', context)

def stats(request):
    adult_squirrels = Squirrel.objects.filter(age = 'Adult').count()
    juvenile_squirrels = Squirrel.objects.filter(age = 'Juvenile').count()
    gray_squirrels = Squirrel.objects.filter(primary_fur_color = 'Gray').count()
    black_squirrels = Squirrel.objects.filter(primary_fur_color = 'Black').count()
    cinnamon_squirrels = Squirrel.objects.filter(primary_fur_color = 'Cinnamon').count()

    context = {
        'adult_squirrels': adult_squirrels,
        'juvenile_squirrels': juvenile_squirrels,
        'gray_squirrels': gray_squirrels,
        'black_squirrels': black_squirrels,
        'cinnamon_squirrels': cinnamon_squirrels,
    }

    return render(request, 'sightings/stats.html', context)

def map(request):
    sightings = Squirrel.objects.all()[:100]
    return render(request, 'sightings/map.html', {'sightings':sightings})
