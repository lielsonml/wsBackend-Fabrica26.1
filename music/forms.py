from django import forms
from .models import Artista, Musicafavorita, Playlist

class ArtistaForm(forms.ModelForm):
    class Meta: 
        model = Artista
        fields = ['nome','genero']

class MusicafavoritaForm(forms.ModelForm):
    class Meta:
        model = Musicafavorita
        fields = ['titulo', 'artista', 'url']

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['nome', 'musicas']