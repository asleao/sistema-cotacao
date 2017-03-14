from rest_framework import serializers
from .models import Cliente, Pedido, Item, Produto


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ('codigo', 'nome')

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ('codigo', 'descricao','marca')

class PedidoSerializer(serializers.ModelSerializer):    
    cliente = ClienteSerializer(read_only=True)
    class Meta:
        model = Pedido
        fields = ('codigo', 'cliente','dataCriacao')

class ItemSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer(read_only=True)
    produto = ProdutoSerializer(read_only=True)
    class Meta:
        model = Item
        fields = ('pedido', 'codigo', 'produto','quantidade')