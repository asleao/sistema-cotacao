angular.module("sistemaFornecedor").service("pedidosAPI",function($http, config){
  
   this.getPedidos = function(){
        return $http.get(config.baseUrl + "/pedido/?format=json");
    };

    this.getItens = function(){
        return $http.get(config.baseUrl + "/item/?format=json");
    };

    this.getPedido = function(id){
        return $http.get(config.baseUrl + "/pedido/"+id+"/?format=json");
    };
});