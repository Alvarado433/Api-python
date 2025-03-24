from Banco.banco import db  # Importando o db corretamente

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    nome = db.Column(db.String(80))
    data_de_nascimento = db.Column(db.Date)
    senha = db.Column(db.String(200))

    def __repr__(self):
        return f"<Usuarios {self.usuario}>"

    def Dados(self):
        return {
            "id": self.id,
            "usuario": self.usuario,
            "email": self.email,
            "nome": self.nome,
            "data_de_nascimento": self.data_de_nascimento,
            "senha": self.senha
        }