from rest_framework import serializers
from .models import Cliente, Pedido, Item


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ('codigo', 'nome')

class PedidoSerializer(serializers.ModelSerializer):    
    cliente = ClienteSerializer()
    class Meta:
        model = Cliente
        fields = ('codigo', 'cliente')

class ItemSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer()
    class Meta:
        model = Item
        fields = ('pedido', 'codigo', 'descricao','marca','quantidade')