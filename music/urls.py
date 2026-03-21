from django.urls import path
from .views import lista_artistas, criar_artista, editar_artista, deletar_artista

urlpatterns = [
    path('lista', lista_artistas, name='lista_artistas'),
    path('criar/', criar_artista, name='criar_artista'),
    path('editar/<int:pk>/', editar_artista, name='editar_artista'),
    path('deletar/<int:pk>/', deletar_artista, name='deletar_artista'),
]
   
