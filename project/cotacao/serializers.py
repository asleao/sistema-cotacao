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
    cliente = ClienteSerializer()
    class Meta:
        model = Pedido
        fields = ('codigo', 'cliente','dataCriacao')
    def create(self, validated_data):
        cliente_data = validated_data.pop('cliente')
        cliente = Cliente.objects.get(nome=cliente_data['nome'])
        pedido= Pedido.objects.create(cliente=cliente)
        return pedido          
       

class ItemSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer()
    produto = ProdutoSerializer()
    class Meta:
        model = Item
        fields = ('pedido', 'codigo', 'produto','quantidade')        
    def create(self, validated_data):
        pedido_data = validated_data.pop('pedido')
        pedido = Pedido.objects.get(codigo=pedido_data['codigo'])        
        produto_data = validated_data.pop('produto')
        produto = Produto.objects.get(codigo=produto_data['codigo'])
        item = Item.objects.create(pedido=pedido,produto=produto)
        return item