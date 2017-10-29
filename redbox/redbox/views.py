from django.shortcuts import render
from .forms import GameForm,MovieForm

def index(request):
    return render(request,'index.html')

def add_game(request):
    # if this is a POST request then we need to process the data
    if request.method == 'POST':
        # create a form instance and populate it with the request data
        form = GameForm(request.POST)
        # check if the form is valid or not
        if form.is_valid():
            # check if the game image exists
            # if 'image' in request.FILES:

            # save the form data to the database
            form.save();
    else:
        form = GameForm()
    return render(request, 'addgame.html', {'form':form})

def add_movie(request):
    # if this is a POST request then we need to process the data
    if request.method == 'POST':
        # create a form instance and populate it with the request data
        form = MovieForm(request.POST)
        # check if the form is valid or not
        if form.is_valid():
            # check if the game image exists
            # if 'image' in request.FILES:

            # save the form data to the database
            form.save();
    else:
        form = MovieForm()
    return render(request, 'addmovie.html', {'form':form})
