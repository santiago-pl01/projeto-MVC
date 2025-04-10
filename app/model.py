import sqlite3

# Classe de conexão com Banco de Dados
class ConexaoBanco:
    def __init__(self, nome_db="dados.db"): # Construtor da classe
        self.nome_db = nome_db
        self.conexao = None
        self.cursor = None
        self.conectar()

    def conectar(self): # Estabelece conexão com o banco e cria o cursor.
        self.conexao = sqlite3.connect(self.nome_db)
        self.cursor = self.conexao.cursor()

    def commit(self): # Salva as alterações no banco.
        if self.conexao:
            self.conexao.commit()
    
    def fechar(self): # Fecha a conexão
        if self.conexao: 
            self.conexao.close()
            self.conexao = None
            self.cursor = None

    def __del__(self): # Destroi o objeto
        self.fechar()



class TabelaBase:

    def __init__(self, nome_db, nome_tabela, campos): # Construtor da classe
        self.nome_tabela = nome_tabela
        self.campos = campos # campos dinamicos
        self.banco = ConexaoBanco(nome_db)
        self.cursor = self.banco.cursor
        self.criar_tabela()

    def criar_tabela(self): # Cria a tabela com campos definidos dinamicamente
        colunas_sql = ", ".join([f"{campo} {tipo}" for campo, tipo in self.campos.items()]) # id é padrão
        sql = f"""
            CREATE TABLE IF NOT EXISTS {self.nome_tabela} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                {colunas_sql}
            )
        """
        self.cursor.execute(sql)
        self.banco.commit()

    def cadastrar(self, **dados): # Cadastra se TODOS os campos forem preenchidos
        if not all(dados.values()):
            print("Todos os campos são obrigatórios")
            return
        try:
            campos = ", ".join(dados.keys())
            valores = tuple(dados.values())
            placeholders = ", ".join(["?"] * len(dados))
            sql = f"INSERT INTO {self.nome_tabela} ({campos}) VALUES ({placeholders})"
            self.cursor.execute(sql, valores)
            self.banco.commit()
            print(f"{self.nome_tabela.capitalize()} cadastrado com sucesso.")
        except sqlite3.IntegrityError:
            print(f"Este {self.nome_tabela} já está cadastrado.")
        except Exception as e:
            print(f"Erro ao cadastrar {self.nome_tabela}:", e)

    def listar(self): # Lista todos os registros da tabela
        self.cursor.execute(f"SELECT * FROM {self.nome_tabela}")
        registros = self.cursor.fetchall()
        if not registros:
            print(f"Nenhum {self.nome_tabela} cadastrado.")
            return
        for linha in registros:
            print(" | ".join([f"{campo}: {valor}" for campo, valor in zip(['id'] + list(self.campos.keys()), linha)]))

    def existe(self, id_): # Confere se o q procura existe no bd. Ultiliza-e o id para procurar.
        self.cursor.execute(f"SELECT 1 FROM {self.nome_tabela} WHERE id = ?", (id_,))
        return self.cursor.fetchone() is not None

    def editar(self, id_, **novos_dados): # Edita os dados dos campos que procura. Ultiliza-se o id para identificar
        if not self.existe(id_):
            print(f"{self.nome_tabela.capitalize()} com id {id_} não encontrado.")
            return
        try:
            campos = [f"{campo} = ?" for campo in novos_dados if novos_dados[campo]]
            valores = [valor for valor in novos_dados.values() if valor]
            if not campos:
                print("Não há dados para editar.")
                return
            sql = f"UPDATE {self.nome_tabela} SET {', '.join(campos)} WHERE id = ?"
            self.cursor.execute(sql, valores + [id_])
            self.banco.commit()
            print(f"{self.nome_tabela.capitalize()} editado com sucesso.")
        except Exception as e:
            print(f"Erro ao editar {self.nome_tabela}:", e)

    def deletar(self, id_): # Deleta TUDO relacionado ao id que selecionou, incluindo o próprio id. O id não é resertado.
        if not self.existe(id_):
            print(f"{self.nome_tabela.capitalize()} com id {id_} não encontrado.")
            return
        try:
            self.cursor.execute(f"DELETE FROM {self.nome_tabela} WHERE id = ?", (id_,))
            self.banco.commit()
            print(f"{self.nome_tabela.capitalize()} deletado com sucesso.")
        except Exception as e:
            print(f"Erro ao deletar {self.nome_tabela}:", e)

    def __del__(self): # Destroi o objeto
        self.banco.fechar()



class Cliente(TabelaBase): # Cria a tabela Cliente
    def __init__(self, nome_db = "dados.db"): # Construtor da classe
        campos = {
            "nome": "TEXT NOT NULL",
            "email": "TEXT NOT NULL UNIQUE",
            "senha": "TEXT NOT NULL"
        }
        super().__init__(nome_db, "usuarios", campos)



class Produto(TabelaBase): # Cria tabela Produto
    def __init__(self, nome_db = "dados.db"): # Construtor da classe
        campos = {
            "nome": "TEXT NOT NULL",
            "marca": "TEXT NOT NULL",
            "data": "INTEGER NOT NULL",
            "quantidade": "INTEGER NOT NULL"
        }
        super().__init__(nome_db, "produtos", campos)