# API de Usuários com Flask

Esta é uma API desenvolvida com Flask que permite realizar operações CRUD (Create, Read, Update, Delete) para gerenciar usuários. A API conecta-se a um banco de dados MySQL e possui as funcionalidades de:

- Criar usuário
- Listar usuários
- Obter um usuário específico
- Editar usuário
- Deletar usuário

## Tecnologias Utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- MySQL
- Flask-CORS

## Instalação

### 1. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv .venv
```

### 2. Ative o ambiente virtual:

Depois de criar o ambiente virtual, é necessário ativá-lo para que as dependências sejam instaladas nesse ambiente isolado.

#### **Windows**:
Para ativar o ambiente virtual no Windows, use o seguinte comando no terminal:

```bash
    .venv\Scripts\activate
```
### 3. Instale as dependências:

Com o ambiente virtual ativo, instale as dependências necessárias para o funcionamento da API utilizando o arquivo `requirements.txt`, que contém todas as bibliotecas necessárias. Execute o seguinte comando:

```bash
pip install -r requirements.txt
```

### 4. Editar o arquivo `.env`

Crie um arquivo `.env` na raiz do seu projeto e adicione as seguintes configurações:

```bash
FLASK_APP=main.py
FLASK_ENV=development
DATABASE_URL='mysql://Usuario:Senha@servidor/nome_banco'
```

### 5. Criar o arquivo `db.py` no diretório `Banco`

No diretório `Banco`, crie um arquivo chamado `db.py` para inicializar a instância do banco de dados. Dentro do arquivo `db.py`, adicione o seguinte código:

```python
from flask_sqlalchemy import SQLAlchemy

# Inicializando a instância do db
db = SQLAlchemy()
```

### 6. Criar o arquivo de configuração `MySQLConfig`

No diretório `Banco`, crie um arquivo chamado `conexao.py` para configurar a conexão com o banco de dados MySQL. Dentro do arquivo `conexao.py`, adicione o seguinte código:

```python
import os

class MySQLConfig:
    # Configuração comum para todos os bancos de dados
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuração específica para o MySQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://Usuario:Senha@servidor/nome_banco')
```

### 7. Criar o Modelo de Usuário

No diretório `models`, crie um arquivo chamado `Usuarios.py` para definir o modelo de dados que será utilizado na API. No arquivo `Usuarios.py`, adicione o seguinte código:

```python
from Banco.banco import db  # Importando o db corretamente

class Usuarios(db.Model):
    # O 'id' será uma chave primária (primary key) e um número inteiro
    id = db.Column(db.Integer, primary_key=True)  # db.Integer define que o campo será um número inteiro

    # O 'usuario' será uma string de até 80 caracteres e precisa ser único
    usuario = db.Column(db.String(80), unique=True, nullable=False)  # db.String define que o campo é uma string com tamanho máximo de 80 caracteres

    # O 'email' será uma string de até 80 caracteres, mas não precisa ser único
    email = db.Column(db.String(80), nullable=False)  # Campo de e-mail, obrigatório e com tamanho máximo de 80 caracteres

    # O 'nome' será uma string de até 80 caracteres e é opcional
    nome = db.Column(db.String(80))  # Campo de nome, com tamanho máximo de 80 caracteres

    # A 'data_de_nascimento' será do tipo Date (data), para armazenar uma data
    data_de_nascimento = db.Column(db.Date)  # db.Date define que o campo será do tipo data

    # A 'senha' será uma string de até 200 caracteres (tamanho maior devido à criptografia da senha)
    senha = db.Column(db.String(200))  # Campo de senha, armazenando até 200 caracteres

    # Método __repr__ é utilizado para representar o objeto em formato de string
    def __repr__(self):
        return f"<Usuarios {self.usuario}>"

    # Método Dados retorna os dados do usuário como um dicionário
    def Dados(self):
        return {
            "id": self.id,  # Retorna o ID do usuário
            "usuario": self.usuario,  # Retorna o nome de usuário
            "email": self.email,  # Retorna o e-mail do usuário
            "nome": self.nome,  # Retorna o nome do usuário
            "data_de_nascimento": self.data_de_nascimento,  # Retorna a data de nascimento
            "senha": self.senha  # Retorna a senha (lembrando que a senha deve ser criptografada antes de ser armazenada)
        }
```