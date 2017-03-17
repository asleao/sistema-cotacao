angular.module("sistemaCompras").controller("pedidoCtrl", function($scope,pedidosAPI,clientesAPI,produtosAPI,pedidos,clientes,produtos){
    $scope.pedidos= pedidos.data;
    $scope.clientes = clientes.data;
    $scope.produtos = produtos.data;	    
});