angular.module("sistemaCompras",["ngMessages","ngRoute"]);
angular.module("sistemaCompras").config(function($httpProvider){      
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';         
});