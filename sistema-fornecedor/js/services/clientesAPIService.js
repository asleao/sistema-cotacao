angular.module("sistemaFornecedor").service("clientesAPI",function($http, config){   

    this.getClientes = function(){
        return $http.get(config.baseUrl +"/cliente/?format=json");
    };
    this.getCliente = function(id){
        return $http.get(config.baseUrl + "/cliente/"+id+"/?format=json");
    };
});