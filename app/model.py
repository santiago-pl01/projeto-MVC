import sqlite3

# Classe de conexão com Banco de Dados

class ConexaoBanco:
    def __init__(self, nome_db = "dados.db"):
        self.nome_db = nome_db
        self.conexao = None
        self.cursor = None
        self.conectar()

    def conectar(self): #  Estabelece conexão com o banco e cria o cursor.
        if self.conexao:
            self.conexao.close()
            self.conexao = None
            self.cursor = None

    def commitar(self): #  Salva as alterações no banco.
        if self.conexao:
            self.conexao.commit()

    def __del__(self):
        self.fechar()

"""### Como usar essa classe em qualquer lugar:###
db = ConexaoBanco("meubanco.db")
db.cursor.execute("CREATE TABLE IF NOT EXISTS exemplo (id INTEGER PRIMARY KEY, nome TEXT)")
db.cursor.execute("INSERT INTO exemplo (nome) VALUES (?)", ("Teste",))
db.commitar()
db.fechar()"""