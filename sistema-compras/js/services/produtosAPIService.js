angular.module("sistemaCompras").service("produtosAPI",function($http, config){   

    this.getProdutos = function(){
        return $http.get(config.baseUrl +"/produto/?format=json");
    };
    this.getProduto = function(id){
        return $http.get(config.baseUrl + "/produto/"+id+"/?format=json");
    };
});