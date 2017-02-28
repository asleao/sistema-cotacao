# Bem Vindo

Este repositório irá desenvolver um sistema web cotação  utilizando a linguagem Python e o framework Django e um sistema de fornecedor utilizando framework AngularJs.

O objetivo deste projeto é fazer com que o sistema de cotação envie um pedido para o fornecedor. A comunicação será feita utilizando o protocolo http onde o sistema cotação disponibiliza
seus pedidos, no formato JSON, e o sistema fornecedor consegue disponibilizar pedidos feitos.

O sistema cotação está hospedado no endereço http://asleao.pythonanywhere.com/admin.

Caso queira realizar a sua configuração em uma máquina, siga o tutorial a seguir. 

Todos os comandos serão executados utilizando um ambiente linux e o editor de texto Sublime Text.

## Pré Requisitos:
	
* **Python3**
* **python3-dev**
* **libpq-dev**
* **Virtualenv**	

## Instalação

### Configuração do ambiente

Faça o download do projeto no [link](https://github.com/asleao/sistema-cotacao.git) ou se possuir o git instalado execute o comando abaixo na pasta em que deseja salvar o projeto.

	git clone https://github.com/asleao/sistema-cotacao.git

Em seguida vá até a pasta onde o projeto foi salvo e crie o ambiente virtual python com o seguinte comando:
	
	virtualenv -p python3 env

Ative-o:

	source env/bin/activate

Instale as dependências:

	pip install -r requirements.txt

Para criar as tabelas no banco, execute o comando:

	python3 manage.py migrate

### Administração

Para criar um usuário adminstrador execute o comando:

	python3 manage.py createsuperuser

### Execução

Para executar o projeto, em um terminal, execute o seguinte comando:

	python3 manage.py runserver



