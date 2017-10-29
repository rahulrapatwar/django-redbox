from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^games/$', views.games, name='games'),
    url(r'^movies/$', views.movies, name='movies'),
]
