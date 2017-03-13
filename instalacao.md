# Instalação do sistema

### Pré Requisitos

* **Python3**
* **python3-dev**
* **libpq-dev**
* **Virtualenv**

### Configuração do ambiente

Faça o download do projeto no [link](https://github.com/asleao/sistema-cotacao.git) ou se possuir o git instalado execute o comando abaixo na pasta em que deseja salvar o projeto.

```bash
git clone https://github.com/asleao/sistema-cotacao.git
```

Em seguida vá até a pasta onde o projeto foi salvo e crie o ambiente virtual python com o seguinte comando:

```bash
virtualenv -p python3 env
```

Ative-o:

```bash
source env/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Para criar as tabelas no banco, execute o comando:

```bash
python3 manage.py migrate
```

#### Administração

Para criar um usuário adminstrador execute o comando:

```bash
python3 manage.py createsuperuser
```

#### Execução

Para executar o projeto, em um terminal, execute o seguinte comando:

```bash
python3 manage.py runserver
```



