from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.db.models import Count, Q

from .models import Squirrel
from .form import SquirrelForm

def index(request):
    return render(request, 'sightings/index.html')

def sightings(request):
    squirrels = Squirrel.objects.all()
    return render(request, '/sightings.html', {'squirrels':squirrels})

def add(request):
    if request.method == "POST":
        new_squirrel = SquirrelForm(request.POST)
        new_squirrel.save()
        return redirect('/sightings/')
    return render(request, 'sightings/add.html')

def detail(request, unique_squirrel_id):
    data = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    if request.method == "POST":
        if 'delete' in request.POST:
            data.delete()
        else:
            data = SquirrelForm(instance=data,data=request.POST)
            data.save()
        return redirect('/sightings/')
    return render(request, 'sightings/detail.html', {'data':data})

def stats(request):
    dataset = Squirrel.objects \
	.values('unique_squirrel_id') \
        .annotate(num_of_squirrels=Count('unique_squirrel_id'),
                adult_squirrels=Count('unique_squirrel_id', filter=Q(age=Adult)),
                juvenile_squirrels=Count('unique_squirrel_id', filter=Q(age=Juvenile)),
		gray_squirrels=Count('unique_squirrel_id', filter=Q(primary_fur_color=Gray)),
                black_squirrels=Count('unique_squirrel_id', filter=Q(primary_fur_color=Black)),
                cinnamon_squirrels=Count('unique_squirrel_id', filter=Q(primary_fur_color=Cinnamon)),
		squirrels_running=Count('unique_squirrel_id', filter=Q(running=True)),
 		squirrels_chasing=Count('unique_squirrel_id', filter=Q(chasing=True)),
		squirrels_foraging=Count('unique_squirrel_id', filter=Q(foraging=True)))
    return render(request, 'sightings/stats.html', {'dataset': dataset})

def map(request):
    xy = list()
    for i in Squirrel.objects.all():
        xy_dict = {}
        xy_dict['latitude']=i.latitude
        xy_dict['longitude']=i.longitude        
        xy.append(xy_dict)
    return render(request, 'sightings/map.html', {'xy':xy})
