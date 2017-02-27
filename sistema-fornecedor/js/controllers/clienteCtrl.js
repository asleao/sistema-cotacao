angular.module("sistemaFornecedor").controller("clienteCtrl", function($scope,clientesAPI,clientes){
    $scope.clientes = clientes.data;     
});