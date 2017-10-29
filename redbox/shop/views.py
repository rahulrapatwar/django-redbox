from django.shortcuts import render
from .models import Game,Movie

# Create your views here.
def games(request,sort):
    if sort == 'alpha':
        games = Game.objects.all().order_by('title')
    elif sort == 'rating':
        games = Game.objects.all().order_by('-rating')
    else:
        games = Game.objects.all()
    return render(request,'shop/store.html',{'games':games})

def movies(request,sort):
    if sort == 'alpha':
        movies = Movie.objects.all().order_by('title')
    elif sort == 'rating':
        movies = Movie.objects.all().order_by('-rating')
    else:
        movies = Movie.objects.all()
    return render(request,'shop/store.html',{'movies':movies})
