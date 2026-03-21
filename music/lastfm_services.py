import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('LASTFM_API_KEY')
URL_BASE = 'http://ws.audioscrobbler.com/2.0/'

def buscar_artista(nome):
    parametros = {
        'method': 'artist.search',
        'artist': nome,
        'api_key': API_KEY,
        'format': 'json',
        'limit': 5,
    }
    resposta = requests.get(URL_BASE, params=parametros)
    resultados = resposta.json()
    return resultados.get('results', {}).get('artistmatches', {}).get('artist', [])

def buscar_musicas(nome):
    parametros = {
        'method': 'track.search',
        'track': nome,
        'api_key': API_KEY,
        'format': 'json',
        'limit': 10,
    }
    resposta = requests.get(URL_BASE, params=parametros)
    resultados = resposta.json()
    return resultados.get('results', {}).get('trackmatches', {}).get('track', [])