from django.shortcuts import render
from rest_framework import generics
from .serializers import ClienteSerializer,ItemSerializer,PedidoSerializer,ProdutoSerializer
from .models import Cliente,Pedido, Item, Produto

# Create your views here.
class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class PedidoList(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer