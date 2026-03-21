from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artistas/novo/', views.artista_criar, name='artista_criar'),
    path('artistas/<int:pk>/editar/', views.artista_editar, name='artista_editar'),
    path('artistas/<int:pk>/deletar/', views.artista_deletar, name='artista_deletar'),

    path('musicas/nova/', views.musica_criar, name='musica_criar'),
    path('musicas/<int:pk>/editar/', views.musica_editar, name='musica_editar'),
    path('musicas/<int:pk>/deletar/', views.musica_deletar, name='musica_deletar'),

     path('lastfm/', views.lastfm_buscar, name='lastfm_buscar'),
    path('lastfm/salvar/', views.lastfm_salvar, name='lastfm_salvar'),

    path('playlists/', views.playlist_listar, name='playlist_listar'),
    path('playlists/nova/', views.playlist_criar, name='playlist_criar'),
    path('playlists/<int:pk>/', views.playlist_detalhe, name='playlist_detalhe'),
    path('playlists/<int:pk>/editar/', views.playlist_editar, name='playlist_editar'),
    path('playlists/<int:pk>/deletar/', views.playlist_deletar, name='playlist_deletar'),
]