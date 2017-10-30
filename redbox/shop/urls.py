from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^games/(?P<sort>\w*)$', views.games, name='games'),
    url(r'^movies/(?P<sort>\w*)$', views.movies, name='movies'),
    url(r'^movie/detail/(?P<pk>\d+)$', views.movie_detail, name='movie_detail'),
    url(r'^game/detail/(?P<pk>\d+)$', views.game_detail, name='game_detail'),
    url(r'^movie/detail/(?P<pk>\d+)/add$', views.add_movie_to_cart, name='add_movie_to_cart'),
]
