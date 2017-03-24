from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
	
    def __str__(self):
        return self.nome

class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=20)  
    marca = models.CharField(max_length=20)    
        
    def __str__(self):
        return self.descricao

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='cliente')         
    codigo = models.AutoField(primary_key=True)   
    dataCriacao = models.DateField(auto_now_add=True)

    def __str__(self): 
        return str(self.codigo)

class Item(models.Model):    
    pedido = models.ForeignKey(Pedido, related_name='pedido',null=True) 
    codigo = models.AutoField(primary_key=True)
    produto = models.ForeignKey(Produto, related_name='produto')
    quantidade = models.PositiveIntegerField(default=0)
    def __str__(self): 
        return str(self.codigo)