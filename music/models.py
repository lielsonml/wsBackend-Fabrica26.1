from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=200)
    spotify_id = models.CharField(max_length=200)
    genero = models.CharField(max_length=80,blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Musicafavorita(models.Model):
    titulo = models.CharField(max_length=200)
    spotify_id = models.CharField(max_length=200)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE,related_name='musicas')
    criado_em = models.DateTimeField(auto_now_add=True)
    duracao_ms = models.IntegerField(default=0)
    url = models.URLField(blank=True, null=True)
   
def __str__(self):
    return f"{self.titulo} - {self.artista.nome}"
    
    

# Create your models here.
