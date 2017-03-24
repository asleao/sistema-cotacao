from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns 
from . import views

urlpatterns = [
	url(r'^cliente/$',views.ClienteList.as_view()),
	url(r'^cliente/(?P<pk>[0-9]+)/$',views.ClienteDetail.as_view()),
	url(r'^pedido/$',views.PedidoList.as_view()),
	url(r'^pedido/(?P<pk>[0-9]+)/$',views.PedidoDetail.as_view()),
	url(r'^item/$',views.ItemList.as_view()),
	url(r'^item/(?P<pk>[0-9]+)/$',views.ItemDetail.as_view()),
	url(r'^produto/$',views.ProdutoList.as_view()),
	url(r'^produto/(?P<pk>[0-9]+)/$',views.ProdutoDetail.as_view()),
	url(r'^pedido/last/$',views.get_pedido_last_id),
]

urlpatterns = format_suffix_patterns(urlpatterns)