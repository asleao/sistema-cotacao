from django.db import models

# Create your models here.

class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
	
    def __str__(self):
        return self.nome


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='cliente')     
    codigo = models.AutoField(primary_key=True)   
    
    def __str__(self): 
        return str(self.codigo)

class Item(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='pedido')
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=20)  
    marca = models.CharField(max_length=20)    
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self): 
        return self.descricao+" "+self.marca




