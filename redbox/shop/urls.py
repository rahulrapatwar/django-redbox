from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^games/(?P<sort>\w*)$', views.games, name='games'),
    url(r'^movies/(?P<sort>\w*)$', views.movies, name='movies'),
]
