# wsBackend-Fabrica26.1
Projeto Django com integração à Spotify Web API.

## Como rodar
1. Clone o repositório
2. Crie e ative o venv
3. `pip install -r requirements.txt`
4. Configure o `.env` com suas credenciais do Spotify
5. `python manage.py migrate`
6. `python manage.py runserver`
```

**`.env`** — crie na raiz (não vai pro git):
```
SPOTIFY_CLIENT_ID=seu_client_id_aqui
SPOTIFY_CLIENT_SECRET=seu_client_secret_aqui