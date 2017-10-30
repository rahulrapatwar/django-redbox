from django.shortcuts import render,get_object_or_404
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

def movie_detail(request,pk):
    # get model with the received pk in the arguments
    movie = get_object_or_404(Movie,pk=pk)
    return render(request, 'shop/detail.html', {'movie':movie})

def game_detail(request,pk):
    # get model with the received pk in the arguments
    game = get_object_or_404(Game,pk=pk)
    return render(request, 'shop/detail.html', {'game':game})

# add movie to the cart
def add_movie_to_cart(request,pk):
    add_movie = get_object_or_404(Movie,pk=pk)
    return render(request, 'shop/detail.html', {'add_movie':add_movie})
