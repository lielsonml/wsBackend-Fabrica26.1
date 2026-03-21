from django.shortcuts import render, get_object_or_404, redirect
from .models import Artista, Musicafavorita, Playlist
from .forms import ArtistaForm, MusicafavoritaForm, PlaylistForm
from .lastfm_services import buscar_artista, buscar_musicas

def home(request):
    artistas = Artista.objects.all()
    musicas = Musicafavorita.objects.select_related('artista').all()
    playlists = Playlist.objects.prefetch_related('musicas').all()
    return render(request, 'music/home.html', {'artistas': artistas,'musicas': musicas, 'playlists': playlists})

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

def lastfm_buscar(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        artistas = []
        musicas = []
        if query:
            artistas = buscar_artista(query)
            musicas = buscar_musicas(query)
        return render(request, 'music/lastfm_buscar.html', {
            'artistas': artistas,
            'musicas': musicas,
            'query': query,
        })
    else:
        return redirect('home')

def lastfm_salvar(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        if tipo == 'artista':
            Artista.objects.get_or_create(
                lastfm_id=request.POST.get('lastfm_id'),
                defaults={
                    'nome': request.POST.get('nome'),
                    'genero': request.POST.get('genero', ''),
                }
            )
            return redirect('home')
        elif tipo == 'musica':
            artista, _ = Artista.objects.get_or_create(
                lastfm_id=request.POST.get('artista_lastfm_id'),
                defaults={'nome': request.POST.get('artista_nome')}
            )
            Musicafavorita.objects.get_or_create(
                lastfm_id=request.POST.get('lastfm_id'),
                defaults={
                    'titulo': request.POST.get('nome'),
                    'artista': artista,
                    'duracao_ms': int(request.POST.get('duracao_ms') or 0),
                    'url': request.POST.get('preview_url', ''),
                }
            )
            return redirect('home')
    else:
        return redirect('lastfm_buscar')
    
def playlist_listar(request):
    playlists = Playlist.objects.all()
    return render(request, 'music/playlist_listar.html', {'playlists': playlists})

def playlist_criar(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playlist_listar')
    else:
        form = PlaylistForm()
    return render(request, 'music/playlist_form.html', {'form': form, 'titulo': 'Nova Playlist'})

def playlist_editar(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    if request.method == 'POST':
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            form.save()
            return redirect('playlist_listar')
    else:
        form = PlaylistForm(instance=playlist)
    return render(request, 'music/playlist_form.html', {'form': form, 'titulo': 'Editar Playlist'})

def playlist_deletar(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    if request.method == 'POST':
        playlist.delete()
        return redirect('playlist_listar')
    return render(request, 'music/playlist_deletar.html', {'playlist': playlist})

def playlist_detalhe(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    return render(request, 'music/playlist_detalhe.html', {'playlist': playlist})