angular.module("sistemaCompras").controller("clienteCtrl", function($scope,clientesAPI,clientes){
    $scope.clientes = clientes.data;     
});