from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate

# Importando o db do arquivo Banco/db.py
from Banco.banco import db
# Importando a classe de configuração
from Banco.conexao import MySQLConfig
# Importando o modelo após a inicialização do db
from models.Usuarios import Usuarios

# Inicializando a aplicação
app = Flask(__name__)

# Configuração do banco de dados utilizando a classe MySQLConfig
app.config.from_object(MySQLConfig)

# Inicializando as extensões
CORS(app)
db.init_app(app)  # Inicializando o db
migrate = Migrate(app, db)

# Rota de exemplo
@app.route('/')
def index():
    return jsonify(message="Api com Flask")

# Listando todos os usuários (GET)
@app.route('/usuarios', methods=['GET'])
def listar():
    usuarios = Usuarios.query.all()  # Pega todos os usuários no banco
    return jsonify([usuario.Dados() for usuario in usuarios]), 200

# Criando um novo usuário (POST)
@app.route('/usuarios', methods=['POST'])
def criar():
    data = request.get_json()

    # Criar um novo usuário
    usuario = Usuarios(
        usuario=data['usuario'],
        email=data['email'],
        nome=data['nome'],
        data_de_nascimento=data['data_de_nascimento'],
        senha=data['senha']
    )

    # Adicionar ao banco de dados
    db.session.add(usuario)
    db.session.commit()

    return jsonify({"message": "Usuário criado com sucesso", "usuario": usuario.usuario}), 201

# Obtendo um usuário específico (GET)
@app.route('/usuarios/<int:id>', methods=['GET'])
def obter_usuario(id):
    usuario = Usuarios.query.get(id)
    if not usuario:
        return jsonify({"message": "Usuário não encontrado"}), 404
    return jsonify(usuario.Dados()), 200

# Editando um usuário (PUT)
@app.route('/usuarios/<int:id>', methods=['PUT'])
def editar(id):
    # Buscando o usuário pelo ID
    usuario = Usuarios.query.get(id)

    if not usuario:
        return jsonify({"message": "Usuário não encontrado"}), 404

    # Recebendo os dados para atualização
    data = request.get_json()

    # Atualizando os campos do usuário
    usuario.usuario = data.get('usuario', usuario.usuario)
    usuario.email = data.get('email', usuario.email)
    usuario.nome = data.get('nome', usuario.nome)
    usuario.data_de_nascimento = data.get('data_de_nascimento', usuario.data_de_nascimento)
    usuario.senha = data.get('senha', usuario.senha)

    # Comitando as mudanças no banco de dados
    db.session.commit()

    return jsonify({"message": "Usuário atualizado com sucesso", "usuario": usuario.usuario}), 200

# Deletando um usuário (DELETE)
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir(id):
    # Procurando o usuário pelo ID
    usuario = Usuarios.query.get(id)

    if not usuario:
        return jsonify({"message": "Usuário não encontrado"}), 404

    # Excluindo o usuário
    db.session.delete(usuario)
    db.session.commit()

    return jsonify({"message": f"Usuário {usuario.usuario} excluído com sucesso!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
