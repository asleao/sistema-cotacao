angular.module("sistemaCompras").controller("pedidoCtrl", function($scope,pedidosAPI,clientesAPI,produtosAPI,pedidos,clientes,produtos,lastId,$location){
    $scope.pedidos= pedidos.data;
    $scope.clientes = clientes.data;
    $scope.produtos = produtos.data;
    $scope.itens=[];
    var id = lastId.data.codigo+1;	


	$scope.adicionarItem = function(item){		
		$scope.itens.push(angular.copy({
              produto: $scope.item.produto,
              quantidade: $scope.item.quantidade
          }));		
		delete $scope.item;
		$scope.formCadastroPedido.$setPristine();
	};

    $scope.cadastrarPedido = function (pedido,itens) {	
    	$scope.pedido.dataCriacao = new Date();
    	$scope.pedido.cliente=$scope.pedido.cliente.codigo;    	
		pedidosAPI.cadastrarPedido(pedido);
		angular.forEach($scope.itens, function(value, key) {		  	  			  
		  var item = {pedido:id,produto:value.produto.codigo,quantidade:value.quantidade}		  	  		  		  
		  pedidosAPI.cadastrarItem(item);
		});						
	};		  
});