# Bem Vindo

Este projeto irá desenvolver um sistema web de cotação utilizando a linguagem Python e o framework Django e um sistema de fornecedor utilizando framework AngularJs que utiliza a linguagem JavaScript.

O objetivo deste projeto é fazer com que o sistema de cotação envie um pedido para o sistema fornecedor. A comunicação será feita utilizando o protocolo http onde o sistema cotação disponibiliza
seus pedidos, no formato JSON, e o sistema fornecedor mostra pedidos feitos.

O sistema cotação está hospedado no endereço http://asleao.pythonanywhere.com/admin. Lá poderão ser feitos os cadastros de novos
Clientes, Produtos, Pedidos e Itens de Pedido. Para acessar os objetos JSON:
 * Com todos os pedidos utilize a url "http://asleao.pythonanywhere.com/cotacao/pedido/?format=json" e um pedido específico utilize a url "http://asleao.pythonanywhere.com/cotacao/pedido/<código_do_pedido>?format=json". 
 * Com todos os itens utilize a url "http://asleao.pythonanywhere.com/cotacao/item/?format=json" e um item específico utilize a url "http://asleao.pythonanywhere.com/cotacao/item/<código_item>?format=json". 
 * Com a lista de clientes utilize a url "http://asleao.pythonanywhere.com/cotacao/cliente/?format=json" e um cliente específico "http://asleao.pythonanywhere.com/cotacao/cliente/<código_cliente>?format=json".

O sistema fornecedor consome os links acima para disponibilizar ao usuário. Para acessá-lo entre na pasta "sistema-fornecedor" e abra o arquivo index.html em um navegador. 

Caso queira realizar a sua configuração em uma máquina, siga o tutorial a seguir. 





