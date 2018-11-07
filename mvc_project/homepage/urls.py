
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.startup, name='startup'),
    path('home', views.homepage, name='home'),
    path('music/album/red', views.album_red, name='red'),
    path('music/album/world', views.album_world, name='world'),
    path('music/album/roads', views.album_roads, name='roads'),
    path('music/album/california', views.album_california, name='california'),
]
