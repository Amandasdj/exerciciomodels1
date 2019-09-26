from django.db import models

# Create your models here.

class Pessoas(models.Model):
   nome = models.CharField(max_length=255,  verbose_name='Nome')
   sobrenome = models.TextField()
   data_de_nascimento = models.DateField()
   cpf = models.CharField(max_length=14)
   cep = models.CharField(max_length=9) 
   item_de_doacao = models.CharField(max_length=255) 

   data_de_criacao =  models.DateTimeField()
   ativo = models.BooleanField(default=True)
