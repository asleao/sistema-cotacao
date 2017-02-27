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
            templateUrl:"view/pedido-detalhe.html" ,
            controller: "paginaPedidoCtrl" ,
            resolve:{
                    receita: function(pedidosAPI, $route){
                            return pedidosAPI.getPedido($route.current.params.id);
                    }
            }
        });


        $routeProvider.otherwise({redirectTo: "/index"});      
});