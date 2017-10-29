from django import forms
from shop.models import Game,Movie

class GameForm(forms.Form):
    class Meta():
        model = Game

class MovieForm(forms.Form):
    class Meta():
        model = Movie
