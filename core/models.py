from django.db import models
from django.contrib.auth.models import User

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.PositiveIntegerField()  # em minutos
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.nome

class Barbeiro(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidades = models.ManyToManyField(Servico)
    
    def __str__(self):
        return self.usuario.get_full_name()
