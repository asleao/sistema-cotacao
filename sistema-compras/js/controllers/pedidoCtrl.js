angular.module("sistemaCompras").controller("pedidoCtrl", function($scope,pedidosAPI,clientesAPI,pedidos){
    $scope.pedidos= pedidos.data;
});