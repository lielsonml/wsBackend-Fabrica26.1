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
    musicas = forms.ModelMultipleChoiceField(
        queryset=Musicafavorita.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Selecione as músicas'
    )
    
    class Meta:
        model = Playlist
        fields = ['nome', 'musicas']