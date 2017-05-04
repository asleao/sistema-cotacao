from django.db import models
from django.utils import timezone
from datetime import date

class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
	
    def __str__(self):
        return self.nome

class UnidadeMedida(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=20)    
    def __str__(self):
        return self.nome

class Quantidade(models.Model):
    codigo = models.AutoField(primary_key=True)
    quantidade = models.CharField(max_length=20)
    unidadeMedida = models.ForeignKey(UnidadeMedida, related_name='unidadeMedida') 
    def __str__(self):
        return self.nome        

class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=20)  
    nomeCurto = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    preco = models.FloatField()
    quantidadeUnitaria = models.ForeignKey(UnidadeMedida, related_name='quantidadeUnitaria')    
    quantidadeEstoque =  models.ForeignKey(Quantidade, related_name='quantidadeEstoque') 
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
    quantidadeUnidades = models.PositiveIntegerField(default=0)
    def __str__(self): 
        return str(self.codigo)

class Vendedor(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    telefone = models.CharField(max_length=12)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome

class FormaPagamento(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
       
    def __str__(self):
        return self.nome

class Cotacao(models.Model):        
    cliente = models.ForeignKey(Cliente, related_name='cliente') 
    vendedor = models.ForeignKey(Vendedor, related_name='vendedor')     
    codigo = models.AutoField(primary_key=True)
    dataCriacao = models.DateField(auto_now_add=True)
    valorPedido = models.FloatField()
    formaPagamento1 = models.ForeignKey(FormaPagamento, related_name='formapagamento1')
    formaPagamento2 = models.ForeignKey(FormaPagamento, related_name='formapagamento2')
    validadeProposta = models.DateField()
    pedido = models.ForeignKey(Pedido, related_name='pedido',null=True) 
    itens = models.ForeignKey(Itens, related_name='itens',null=True)        
    def __str__(self): 
        return str(self.codigo)