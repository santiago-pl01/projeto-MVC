import sqlite3

# Classe de conexão com Banco de Dados

class ConexaoBanco:
    def __init__(self, nome_db = "dados.db"): # construtor da classe
        self.nome_db = nome_db
        self.conexao = None
        self.cursor = None
        self.conectar()

    def conectar(self): #  Estabelece conexão com o banco e cria o cursor.
        self.conexao = sqlite3.connect(self.nome_db)
        self.cursor = self.conexao.cursor()

    def commit(self): #  Salva as alterações no banco.
        if self.conexao:
            self.conexao.commit()
    
    def fechar(self): # Fecha a conexão
        if self.conexao:
            self.conexao.close()
            self.conexao = None
            self.cursor = None

    def __del__(self): # destroi o objeto
        self.fechar()

"""### Como usar essa classe em qualquer lugar:###
db = ConexaoBanco("meubanco.db")
db.cursor.execute("CREATE TABLE IF NOT EXISTS exemplo (id INTEGER PRIMARY KEY, nome TEXT)")
db.cursor.execute("INSERT INTO exemplo (nome) VALUES (?)", ("Teste",))
db.commitar()
db.fechar()"""








class Cliente:
    
    def __init__(self, nome_db = "dados.db"):
        # cria uma instância  da ConexaoBanco
        self.banco = ConexaoBanco(nome_db)
        self.cursor = self.banco.cursor 
        self.criar_tabela() # se não existir

    def criar_tabela(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS usuarios(
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            senha TEXT NOT NULL)
                            """)
        self.banco.commit()
    
    def cadastrar_cliente(self, nome, email, senha): # espera-se receber nome, email e senha para cadastrar
        try:
            self.cursor.execute("""
                                INSERT INTO usuarios (nome, email, senha)
                                VALUES (?, ?, ?)
                                """, (nome, email, senha))
            self.banco.commit()
            print("Cliente cadastrado com sucesso.")
        except sqlite3.IntegrityError:
            print("Este cliente já está cadastrado")
        except Exception as e:
            print("Erro ao cadastrar o cliente:", e)
    
    def listar_cliente(self): # Buscar os dados do cliente (forma de lista)
        self.cursor.execute("SELECT id, nome, email FROM usuarios")
        usuarios = self.cursor.fetchall()
        for usuario in usuarios: 
            print(usuario)

    def __del__(self):
        self.banco.fechar()