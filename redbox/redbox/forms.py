from django import forms
from shop.models import Game,Movie

class GameForm(forms.ModelForm):
    class Meta():
        model = Game
        fields = ('title','description','genre','rating','image')

class MovieForm(forms.ModelForm):
    class Meta():
        model = Movie
        fields = ('title','description','genre','rating','image')
