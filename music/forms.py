from django import forms
from .models import Artista, Musicafavorita

class ArtistaForm(forms.ModelForm):
    class Meta: 
        model = Artista
        fields = ['nome','genero']

class MusicafavoritaForm(forms.ModelForm):
    class Meta:
        model = Musicafavorita
        fields = ['titulo', 'artista', 'url']