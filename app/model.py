import sqlite3

class ConexaoBanco:
    """
    Classe responsável por gerenciar a conexão com o banco de dados SQLite.
    """

    def __init__(self, nome_db="dados.db"):
        """
        Inicializa a conexão com o banco de dados e cria o cursor.

        Parâmetros:
        nome_db (str): Nome do arquivo do banco de dados SQLite. Padrão: "dados.db".
        """
        self.nome_db = nome_db
        self.conexao = None
        self.cursor = None
        self.conectar()

    def conectar(self):
        """
        Estabelece a conexão com o banco de dados e cria o cursor.
        """
        self.conexao = sqlite3.connect(self.nome_db)
        self.cursor = self.conexao.cursor()

    def commit(self):
        """
        Salva (confirma) as alterações feitas no banco de dados.
        """
        if self.conexao:
            self.conexao.commit()
    
    def fechar(self):
        """
        Fecha a conexão com o banco de dados.
        """
        if self.conexao: 
            self.conexao.close()
            self.conexao = None
            self.cursor = None

    def __del__(self):
        """
        Finaliza o objeto e garante o fechamento da conexão com o banco.
        """
        self.fechar()


class TabelaBase:
    """
    Classe base para criação e manipulação de tabelas no banco de dados.
    Deve ser herdada por classes específicas como Cliente ou Produto.
    """

    def __init__(self, nome_db, nome_tabela, campos):
        """
        Inicializa a tabela com os campos especificados e cria-a caso não exista.

        Parâmetros:
        nome_db (str): Nome do banco de dados.
        nome_tabela (str): Nome da tabela a ser criada/manipulada.
        campos (dict): Dicionário com os nomes dos campos e seus tipos (ex: {"nome": "TEXT"}).
        """
        self.nome_tabela = nome_tabela
        self.campos = campos
        self.banco = ConexaoBanco(nome_db)
        self.cursor = self.banco.cursor
        self.criar_tabela()

    def criar_tabela(self):
        """
        Cria a tabela no banco de dados com os campos definidos dinamicamente.
        """
        colunas_sql = ", ".join([f"{campo} {tipo}" for campo, tipo in self.campos.items()])
        sql = f"""
            CREATE TABLE IF NOT EXISTS {self.nome_tabela} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                {colunas_sql}
            )
        """
        self.cursor.execute(sql)
        self.banco.commit()

    def cadastrar(self, **dados):
        """
        Cadastra um novo registro na tabela.

        Parâmetros:
        dados (dict): Dados a serem inseridos na tabela, onde as chaves são os nomes dos campos.
        """
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

    def listar(self):
        """
        Lista todos os registros da tabela no console.
        """
        self.cursor.execute(f"SELECT * FROM {self.nome_tabela}")
        registros = self.cursor.fetchall()
        if not registros:
            print(f"Nenhum {self.nome_tabela} cadastrado.")
            return 
        for linha in registros:
            print(" | ".join([f"{campo}: {valor}" for campo, valor in zip(['id'] + list(self.campos.keys()), linha)]))

    def existe(self, id_,):
        """
        Verifica se um registro com o ID informado existe na tabela.

        Parâmetros:
        id_ (int): Identificador do registro.

        Retorna:
        bool: True se o registro existe, False caso contrário.
        """
        self.cursor.execute(f"SELECT 1 FROM {self.nome_tabela} WHERE id = ?", (id_,))
        return self.cursor.fetchone() is not None

    def editar(self, id_, **novos_dados):
        """
        Edita os campos de um registro existente com base no ID.

        Parâmetros:
        id_ (int): Identificador do registro a ser editado.
        novos_dados (dict): Campos a serem atualizados e seus novos valores.
        """
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

    def deletar(self, id_):
        """
        Deleta um registro da tabela com base no ID.

        Parâmetros:
        id_ (int): Identificador do registro a ser excluído.
        """
        if not self.existe(id_):
            print(f"{self.nome_tabela.capitalize()} com id {id_} não encontrado.")
            return
        try:
            self.cursor.execute(f"DELETE FROM {self.nome_tabela} WHERE id = ?", (id_,))
            self.banco.commit()
            print(f"{self.nome_tabela.capitalize()} deletado com sucesso.")
        except Exception as e:
            print(f"Erro ao deletar {self.nome_tabela}:", e)

    def __del__(self):
        """
        Finaliza o objeto e garante o fechamento do banco.
        """
        self.banco.fechar()


class Cliente(TabelaBase):
    """
    Classe que representa a tabela de usuários (clientes) no banco de dados.
    Herda os métodos da classe TabelaBase.
    """

    def __init__(self, nome_db="dados.db"):
        """
        Inicializa a tabela de clientes com os campos nome, email e senha.
        
        Parâmetros:
        nome_db (str): Nome do banco de dados. Padrão: "dados.db".
        """
        campos = {
            "nome": "TEXT NOT NULL",
            "email": "TEXT NOT NULL UNIQUE",
            "senha": "TEXT NOT NULL UNIQUE"
        }
        super().__init__(nome_db, "usuarios", campos)


class Produto(TabelaBase):
    """
    Classe que representa a tabela de produtos no banco de dados.
    Herda os métodos da classe TabelaBase.
    """

    def __init__(self, nome_db="dados.db"):
        """
        Inicializa a tabela de produtos com os campos nome, marca, data e quantidade.
        
        Parâmetros:
        nome_db (str): Nome do banco de dados. Padrão: "dados.db".
        """
        campos = {
            "nome": "TEXT NOT NULL",
            "marca": "TEXT NOT NULL",
            "data": "INTEGER NOT NULL",
            "quantidade": "INTEGER NOT NULL",
            "preço": "INTEGER NOT NULL"
        }
        super().__init__(nome_db, "produtos", campos)