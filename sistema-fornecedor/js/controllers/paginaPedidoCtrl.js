angular.module("sistemaFornecedor").controller("paginaPedidoCtrl", function($scope,$routeParams,pedidosAPI,pedido,itens){
    $scope.pedido= pedido.data;      
    $scope.itens = itens.data;		
});
