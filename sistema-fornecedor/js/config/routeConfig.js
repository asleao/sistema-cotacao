angular.module("sistemaFornecedor").config(function($routeProvider){
        
        $routeProvider.when("/clientes",{
            templateUrl:"view/cliente.html" ,
            controller: "clienteCtrl" ,
            resolve:{
                    clientes: function(clientesAPI){
                            return clientesAPI.getClientes();
                    }
            }             
        });
         
        $routeProvider.when("/pedidos",{
            templateUrl:"view/pedidos.html" ,
            controller: "pedidoCtrl" ,
            resolve:{
                    pedidos: function(pedidosAPI){
                            return pedidosAPI.getPedidos();
                    }
            }             
        });
        
        $routeProvider.when("/pedido/:id",{
            templateUrl:"view/pedidosDetalhe.html" ,
            controller: "paginaPedidoCtrl" ,
            resolve:{
                    pedido: function(pedidosAPI, $route){
                            return pedidosAPI.getPedido($route.current.params.id);
                    },
                    itens: function(pedidosAPI){
                            return pedidosAPI.getItens();
                    }
            }
        });


        $routeProvider.otherwise({redirectTo: "/index"});      
});