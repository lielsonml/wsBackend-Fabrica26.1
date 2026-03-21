from django.shortcuts import render, get_object_or_404, redirect
from .models import Artista, Musicafavorita
from .forms import ArtistaForm, MusicafavoritaForm

def home(request):
    artistas = Artista.objects.all()
    musicas = Musicafavorita.objects.select_related('artista').all()
    return render(request, 'music/home.html', {'artistas': artistas,'musicas': musicas,})

def artista_criar(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArtistaForm()
    return render(request, 'music/form_artista.html', {'form': form, 'titulo': 'Novo Artista'})

def artista_editar(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'music/form_artista.html', {'form': form, 'titulo': 'Editar Artista'})

def artista_deletar(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        artista.delete()
        return redirect('home')
    return render(request, 'music/deletar_artista.html', {'artista': artista})

def musica_criar(request):
    if request.method == 'POST':
        form = MusicafavoritaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MusicafavoritaForm()
    return render(request, 'music/form_musica.html', {'form': form, 'titulo': 'Nova Música'})

def musica_editar(request, pk):
    musica = get_object_or_404(Musicafavorita, pk=pk)
    if request.method == 'POST':
        form = MusicafavoritaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MusicafavoritaForm(instance=musica)
    return render(request, 'music/form_musica.html', {'form': form, 'titulo': 'Editar Música'})

def musica_deletar(request, pk):
    musica = get_object_or_404(Musicafavorita, pk=pk)
    if request.method == 'POST':
        musica.delete()
        return redirect('home')
    return render(request, 'music/deletar_musica.html', {'musica': musica})