from django.db import models
from django.utils import timezone

# aqui vai ser criado  as classes de meu site !!!

# criar filme

LISTA_CATEGORIA = (
    ('ANALISES', 'Análises'),
    ('PROGRAMACAO', 'Programação'),
    ('APRESENTACAO', 'Apresentação'),
    ('OUTROS', 'Outros'),
)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    thumbnail = models.ImageField(upload_to='thumb_filmes')
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIA)
    data_criacao = models.DateTimeField(default=timezone.now)
    visualizacao = models.IntegerField(default=0)


    def __str__(self):
        return self.titulo


# criar episodio



