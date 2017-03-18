angular.module("sistemaCompras").controller("pedidoCtrl", function($scope,pedidosAPI,clientesAPI,produtosAPI,pedidos,clientes,produtos,$location){
    $scope.pedidos= pedidos.data;
    $scope.clientes = clientes.data;
    $scope.produtos = produtos.data;
    $scope.itens=[];

	$scope.adicionarItem = function(item){
		$scope.itens.push(angular.copy(item));		
		delete $scope.item;
		$scope.formCadastroPedido.$setPristine();
	};

    $scope.cadastrarPedido = function (pedido,itens) {	
    	pedido.dataCriacao = new Date();
		pedidosAPI.cadastrarPedido(pedido).success(function (data) {

		});		
		pedidosAPI.cadastrarItens(itens).success(function (data) {

		});
	};		  
});