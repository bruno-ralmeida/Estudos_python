from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    def __str__(self):
        #Mostrando o nome da pessoa no Django admin para adicionar receita
        return self.nome 