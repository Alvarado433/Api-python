import os


class MySQLConfig:
    # Configuração comum para todos os bancos de dados
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuração específica para o MySQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://Rhaian:Alvarado209@localhost/Api_teste')
