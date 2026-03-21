from django.shortcuts import render, get_object_or_404, redirect
from .models import Artista, Musicafavorita
from .forms import ArtistaForm, MusicafavoritaForm

def lista_artistas(request):
    artistas = Artista.objects.all()
    return render(request, 'music/lista_artistas.html', {'artistas': artistas})

def criar_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_artistas')
    else:
        form = ArtistaForm()
    return render(request,'music/form_artista.html',{'form': form, 'titulo': 'Criar Artista'},)

def editar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('lista_artistas')
    else:
        form = ArtistaForm(instance=artista)
    return render(request,'music/form_artista.html',{'form': form, 'titulo': 'Editar Artista'},)

def deletar_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == 'POST':
        artista.delete()
        return redirect('lista_artistas')
    return render(request, 'music/deletar_artista.html', {'artista': artista})

def lista_musicas(request):
    musicas = Musicafavorita.objects.all()
    return render(request, 'music/lista_musicas.html', {'musicas': musicas})

def criar_musica(request):
    if request.method == 'POST':
        form = MusicafavoritaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_musicas')
    else:
        form = MusicafavoritaForm()
    return render(request, 'music/form_musica.html', {'form': form, 'titulo': 'Criar Música'},)

def editar_musica(request, pk):
    musica = get_object_or_404(Musicafavorita, pk=pk)
    if request.method == 'POST':
        form = MusicafavoritaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('lista_musicas')
    else:
        form = MusicafavoritaForm(instance=musica)
    return render(request, 'music/form_musica.html', {'form': form, 'titulo': 'Editar Música'},)

def deletar_musica(request, pk):
    musica = get_object_or_404(Musicafavorita, pk=pk)
    if request.method == 'POST':
        musica.delete()
        return redirect('lista_musicas')
    return render(request, 'music/deletar_musica.html', {'musica': musica}) 




    

    
