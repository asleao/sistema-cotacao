angular.module("sistemaFornecedor").controller("pedidoCtrl", function($scope,pedidosAPI,clientesAPI,pedidos){
    $scope.pedidos= pedidos.data;      
});