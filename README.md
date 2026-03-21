# SoundTrackr 🎵

> Sistema de gerenciamento musical com integração à Last.fm API — desenvolvido para a Fábrica de Software 26.1.

🐍 Python 3.13   |   🌐 Django 6.0.3   |   🗄️ MySQL 8.0   |   🎵 Last.fm API   |   🐳 Docker

---

## 👤 Criador

| Campo | Info |
|-------|------|
| **Nome** | Lielson Marques de Lacerda |
| **RGM** | 42991129 |

---

## 💡 Sobre o Projeto

O **SoundTrackr** é uma aplicação web construída com Django que permite gerenciar sua biblioteca musical pessoal. Você pode cadastrar artistas e músicas manualmente, ou buscar diretamente pela **Last.fm API** e salvar com um clique. Também é possível criar playlists personalizadas com as músicas que você já tem no sistema.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
|------------|--------|
| Python 3.13 | Linguagem principal |
| Django 6.0.3 | Framework web |
| MySQL 8.0 | Banco de dados |
| mysqlclient | Conector MySQL |
| python-dotenv | Leitura de variáveis de ambiente |
| requests | Requisições HTTP para a API |
| Last.fm API | API externa de música |
| Docker | Containerização da aplicação |

---

## ✨ Recursos

### 🎤 Artistas
- **+ Novo Artista** — cadastra um artista manualmente com nome e gênero
- **Editar** — atualiza as informações de um artista já cadastrado
- **Excluir** — remove o artista e todas as músicas vinculadas a ele

### 🎵 Músicas
- **+ Nova Música** — cadastra uma música manualmente vinculada a um artista
- **Editar** — atualiza as informações de uma música
- **Excluir** — remove a música do banco de dados
- **Duração formatada** — exibe a duração em minutos e segundos (ex: 3:45)

### 📋 Playlists
- **+ Nova Playlist** — cria uma playlist com nome, descrição e músicas
- **Ver** — exibe todas as músicas dentro da playlist
- **Editar** — adiciona ou remove músicas da playlist
- **Excluir** — remove a playlist

### 🔍 Busca via Last.fm API
- Busca artistas e músicas diretamente na Last.fm API
- Exibe os resultados em tempo real
- Salva artistas e músicas no banco com um clique
- Duração e URL são preenchidos automaticamente pela API

---

## 🗄️ Entidades do Banco de Dados
```
Artista (1) ──────────── (N) MusicaFavorita
                                  │
                                  │ (N)
                                  │
                             Playlist (1)
```

| Entidade | Campos principais |
|----------|------------------|
| `Artista` | nome, genero, spotify_id |
| `MusicaFavorita` | titulo, artista, duracao_ms, url |
| `Playlist` | nome, musicas |

---

## 📁 Organização dos Arquivos
```
wsBackend-Fabrica26.1/
├── core/                   # configurações do projeto
│   ├── settings.py         # banco, apps, configurações gerais
│   └── urls.py             # roteador principal
├── music/                  # app principal
│   ├── templates/music/    # arquivos HTML
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── lastfm_buscar.html
│   │   ├── playlist_listar.html
│   │   └── ...
│   ├── static/music/css/   # arquivos CSS
│   ├── models.py           # entidades do banco
│   ├── views.py            # lógica das páginas
│   ├── forms.py            # formulários
│   ├── urls.py             # rotas do app
│   └── lastfm_service.py   # integração Last.fm API
├── .env                    # variáveis de ambiente (não vai pro GitHub)
├── .env.example            # modelo de variáveis
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## 🚀 Como Instalar e Executar

### ▶️ Opção 1 — Executar localmente

#### 1 — Clone o repositório
```bash
git clone https://github.com/seu-usuario/wsBackend-Fabrica26.1.git
cd wsBackend-Fabrica26.1
```

#### 2 — Crie e ative o ambiente virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

#### 3 — Instale as dependências
```bash
pip install -r requirements.txt
```

#### 4 — Configure o arquivo .env
Crie um arquivo `.env` baseado no `.env.example`:
```
LASTFM_API_KEY=sua_api_key_aqui
MYSQL_PASSWORD=sua_senha_mysql
```

#### 5 — Crie o banco de dados no MySQL
```sql
CREATE DATABASE spotify_manager;
```

#### 6 — Rode as migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 7 — Inicie o servidor
```bash
python manage.py runserver
```

Acesse em `http://127.0.0.1:8000/` 🎉

---

### 🐳 Opção 2 — Executar com Docker

#### 1 — Clone o repositório
```bash
git clone https://github.com/seu-usuario/wsBackend-Fabrica26.1.git
cd wsBackend-Fabrica26.1
```

#### 2 — Configure o arquivo .env
```
LASTFM_API_KEY=sua_api_key_aqui
MYSQL_PASSWORD=sua_senha_mysql
```

#### 3 — Suba os containers
```bash
docker-compose up
```

Acesse em `http://127.0.0.1:8000/` 🎉

---

## 🗺️ Rotas Disponíveis

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | 🏠 Página principal |
| `/artistas/novo/` | GET/POST | ➕ Cadastra novo artista |
| `/artistas/<pk>/editar/` | GET/POST | ✏️ Edita artista |
| `/artistas/<pk>/deletar/` | GET/POST | ❌ Deleta artista |
| `/musicas/nova/` | GET/POST | ➕ Cadastra nova música |
| `/musicas/<pk>/editar/` | GET/POST | ✏️ Edita música |
| `/musicas/<pk>/deletar/` | GET/POST | ❌ Deleta música |
| `/playlists/` | GET | 📋 Lista playlists |
| `/playlists/nova/` | GET/POST | ➕ Cria playlist |
| `/playlists/<pk>/` | GET | 👁️ Detalhe da playlist |
| `/playlists/<pk>/editar/` | GET/POST | ✏️ Edita playlist |
| `/playlists/<pk>/deletar/` | GET/POST | ❌ Deleta playlist |
| `/lastfm/` | GET | 🔍 Busca na Last.fm API |
| `/lastfm/salvar/` | POST | 💾 Salva resultado da API |

---

## 📝 Padrão de Commits

| Tipo | Quando usar |
|------|------------|
| `feat:` | Nova funcionalidade |
| `chore:` | Configuração e arquivos de suporte |
| `docs:` | Documentação |
| `fix:` | Correção de bug |
| `refactor:` | Melhoria de código sem mudar funcionalidade |
| `style:` | Alterações visuais |

---

## 🧠 Uso de Inteligência Artificial no Desenvolvimento

- **Organização do README** — auxiliou na estruturação e formatação da documentação do projeto
- **Explicação de conceitos da API** — explicou o funcionamento da Last.fm API, como autenticação, endpoints de busca e estrutura do JSON retornado
- **Identificação de erros no código** — ajudou a identificar e corrigir erros encontrados durante o desenvolvimento
- **Front-end com CSS e JS** — auxiliou na criação da interface visual do projeto com HTML, CSS e JavaScript


