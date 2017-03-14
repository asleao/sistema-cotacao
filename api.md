# Documentação da API:

Este documento será responsável por mostrar quais são as rotas e operações que poderão ser utilizadas na API desenvolvida.

O sistema cotação está hospedado no endereço [http://asleao.pythonanywhere.com/](http://asleao.pythonanywhere.com/admin). A comunicação com esta aplicação será feita utilizando JSON.Ou seja, os métodos GET retornarão objetos JSON e os métodos POST devem ser feito utilizando o mesmo padrão.

Abaixo a lista de rodas disponibilizadas:

**Produto\(String descricao,String marca\):**

**GET:**

* Listagem de todos os produtos:[http://asleao.pythonanywhere.com/cotacao/produto/?format=json](http://asleao.pythonanywhere.com/cotacao/cliente/?format=json)
* Listagem de 1 produto espercífico: [http://asleao.pythonanywhere.com/cotacao/](http://asleao.pythonanywhere.com/cotacao/cliente/<código_cliente>/?format=json)[produto](http://asleao.pythonanywhere.com/cotacao/cliente/?format=json)[/&lt;código\_produto&gt;/?format=json](http://asleao.pythonanywhere.com/cotacao/cliente/<código_cliente>/?format=json)

**POST:**

* Inserir novo Produto:[http://asleao.pythonanywhere.com/cotacao/produto/?format=json](http://asleao.pythonanywhere.com/cotacao/cliente/?format=json)

**Cliente\(String nome\):**

**GET:**

* Listagem de todos os clientes:[http://asleao.pythonanywhere.com/cotacao/cliente/?format=json](http://asleao.pythonanywhere.com/cotacao/cliente/?format=json)
* Listagem de 1 cliente espercífico: [http://asleao.pythonanywhere.com/cotacao/cliente/&lt;código\_cliente&gt;/?format=json](http://asleao.pythonanywhere.com/cotacao/cliente/<código_cliente>/?format=json)

**POST:**

* Inserir novo cliente:[http://asleao.pythonanywhere.com/cotacao/cliente/?format=json](http://asleao.pythonanywhere.com/cotacao/cliente/?format=json)

**Pedido\(Cliente cliente, Date dataCriacao\):**

**GET:**

* Listagem de todos os pedidos: [http://asleao.pythonanywhere.com/cotacao/pedido/?format=json](http://asleao.pythonanywhere.com/cotacao/pedido/?format=json)
* Listagem de 1 pedido específico: [http://asleao.pythonanywhere.com/cotacao/pedido/&lt;código\_do\_pedido&gt;/?format=json](http://asleao.pythonanywhere.com/cotacao/pedido/<código_do_pedido>/?format=json)
* Formato da data: YYYY-MM-DD

**POST:**

* Inserir novo pedido:[http://asleao.pythonanywhere.com/cotacao/pedido/?format=json](http://asleao.pythonanywhere.com/cotacao/cliente/?format=json)

**Itens\(Pedido pedido,Produto produto, Integer quantidade\):**

**GET:**

* Listagem de todos os itens: [http://asleao.pythonanywhere.com/cotacao/item/?format=json](http://asleao.pythonanywhere.com/cotacao/item/?format=json)
* Listagem de 1 item específico: [http://asleao.pythonanywhere.com/cotacao/item/&lt;código\_item&gt;/?format=json](http://asleao.pythonanywhere.com/cotacao/item/<código_item>/?format=json)

**POST:**

* Inserir novo item:[http://asleao.pythonanywhere.com/cotacao/item/?format=json](http://asleao.pythonanywhere.com/cotacao/cliente/?format=json)



