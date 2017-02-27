from django.shortcuts import render
from rest_framework import generics
from .serializers import ClienteSerializer,ItemSerializer,PedidoSerializer
from .models import Cliente,Pedido, Item

# Create your views here.
class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


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