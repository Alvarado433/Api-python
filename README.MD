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

### 8) Como Fazer as Migrações no Python

As migrações permitem que você altere o banco de dados de maneira controlada, sem perder dados. Usamos o **Flask-Migrate** e o **Alembic** para gerenciar as migrações no Flask.

#### 1. Instalar Flask-Migrate

Se você ainda não instalou o **Flask-Migrate**, instale-o com o comando:

```bash
pip install Flask-Migrate
```
### 2) Inicializando as Migrações

Para inicializar as migrações no seu projeto, siga os passos abaixo:

1. Certifique-se de que você já tenha o **Flask-Migrate** instalado e configurado corretamente (como mostrado na seção anterior).

   2. No diretório do seu projeto, onde o arquivo `main.py` está localizado, execute o comando:

       ```bash
       flask db init
       ```

       Este comando criará o diretório `migrations/` no seu projeto, onde todas as migrações serão armazenadas. Este diretório irá conter arquivos e scripts que controlam as alterações no banco de dados.

   3. Após executar o comando acima, você verá a seguinte estrutura de diretórios no seu projeto:

       ```
       migrations/
       ├── env.py
       ├── README
       ├── script.py.mako
       └── versions/
       ```

       - O arquivo `env.py` contém a configuração necessária para o Alembic, que é a ferramenta usada pelo Flask-Migrate para controlar as migrações.
       - O diretório `versions/` é onde serão armazenados os arquivos de migração gerados.

Com isso, você terá inicializado com sucesso o sistema de migrações no seu projeto.

### 4) Criar a Primeira Migração

Após inicializar o sistema de migrações, você pode criar a primeira migração para refletir as alterações no seu modelo de dados (como criar as tabelas no banco de dados).

1. Execute o seguinte comando para criar a primeira migração:

    ```bash
    flask db migrate -m "Initial migration"
    ```

    - O `-m` é utilizado para adicionar uma mensagem de descrição da migração, que pode ser algo como "Initial migration" (ou qualquer outra descrição que faça sentido para a alteração).
    - O comando acima verifica as alterações no seu modelo de dados e gera automaticamente o arquivo de migração no diretório `migrations/versions`.

   2. Após o comando ser executado, você verá um novo arquivo gerado no diretório `migrations/versions/`. Este arquivo contém o código necessário para atualizar o banco de dados de acordo com o modelo.

       Exemplo de arquivo gerado:

       ```
       migrations/
       └── versions/
           └── 12345abcde_create_users_table.py
       ```

   3. O arquivo gerado conterá o código que reflete as alterações no modelo de dados. Esse código será utilizado para alterar o banco de dados, criando tabelas e colunas, ou fazendo outras alterações necessárias.

#### 5. Aplicar as Migrações no Banco de Dados

Após criar a migração, é necessário aplicá-la ao banco de dados para que as mudanças feitas no modelo de dados sejam refletidas no banco.

1. Para aplicar a migração, execute o seguinte comando:

    ```bash
    flask db upgrade
    ```

    Esse comando aplica todas as migrações pendentes no banco de dados.

   2. Após rodar o comando, o banco de dados será atualizado conforme as migrações criadas. Isso pode incluir a criação de tabelas, alteração de colunas e outros ajustes necessários.

Agora seu banco de dados está atualizado e pronto para ser usado com as novas alterações de modelo.


### Visualizando as Tabelas Criadas Após a Migração

Após aplicar as migrações no banco de dados com o comando `flask db upgrade`, você pode verificar as tabelas criadas diretamente no seu banco de dados MySQL.

#### Usando o MySQL Workbench ou Cliente de Banco de Dados

Se você estiver utilizando o **MySQL Workbench** ou outro cliente de banco de dados, basta abrir a conexão com o banco e visualizar as tabelas criadas.

**Passos no MySQL Workbench:**

1. Abra o **MySQL Workbench**.
2. Conecte-se ao seu banco de dados, utilizando as credenciais configuradas no seu arquivo `.env`.
3. Na guia **Schemas**, você verá a base de dados (neste caso, `Api_teste` ou o nome que você configurou).
4. Expanda o banco de dados para visualizar as tabelas criadas, como a tabela `usuarios`, se você seguiu o modelo de exemplo.

#### Usando o Terminal

Você também pode usar o terminal para verificar as tabelas com o comando SQL:

1. Abra o terminal do MySQL:

    ```bash
    mysql -u Root -p
    ```

2. Após digitar a senha, acesse o banco de dados:

    ```sql
    USE Api_teste;
    ```

3. Para listar todas as tabelas, execute o comando:

    ```sql
    SHOW TABLES;
    ```

Isso irá exibir todas as tabelas criadas, incluindo as que foram adicionadas ou modificadas pelas migrações.

**Exemplo de saída do comando `SHOW TABLES`:**
![img_1.png](img_1.png)


