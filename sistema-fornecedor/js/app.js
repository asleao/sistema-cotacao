angular.module("sistemaFornecedor",["ngMessages","ngRoute"]);
angular.module("sistemaFornecedor").config(function($httpProvider){      
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';         
});