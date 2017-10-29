from django.shortcuts import render
from .models import Game,Movie

# Create your views here.
def games(request):
    games = Game.objects.all()
    return render(request,'shop/store.html',{'games':games})

def movies(request):
    movies = Movie.objects.all()
    return render(request,'shop/store.html',{'movies':movies})
