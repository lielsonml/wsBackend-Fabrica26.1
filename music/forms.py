from django import forms
from .models import Artista, Musicafavorita

class ArtistaForm(forms.ModelForm):
    class Meta: 
        model = Artista
        fields = ['nome', 'spotify_id', 'genero']

class MusicafavoritaForm(forms.ModelForm):
    class Meta:
        model = Musicafavorita
        fields = ['titulo', 'spotify_id', 'artista', 'duracao_ms', 'url']