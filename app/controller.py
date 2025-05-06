from model import Usuario, Produto

# ---------- USUÁRIO (Cliente) ----------

def cadastrar_usuario(nome, email, senha):
    try:
        usuario = Usuario()
        usuario.cadastrar(nome=nome, email=email, senha=senha)
        return "Usuário cadastrado com sucesso."
    except Exception as e:
        return f"Erro ao cadastrar usuário: {e}"
    finally:
        del usuario  # Garante fechamento da conexão

def editar_usuario(id, nome, email, senha):
    try:
        usuario = Usuario()
        Usuario.editar(id, nome=nome, email=email, senha=senha)
        return "Usuário editado com sucesso."
    except Exception as e:
        return f"Erro ao editar usuário: {e}"
    finally:
        del usuario

def deletar_usuario(id):
    try:
        usuario = Usuario()
        usuario.deletar(id)
    except Exception as e:
        print(f"Erro ao excluir usuário: {e}")
    finally:
        del usuario

def listar_usuario():
    try:
        usuario = Usuario()
        usuario = usuario.listar() 
        return usuario
    except Exception as e:
        print(f"Erro ao listar usuários: {e}")
        return []
    finally:
        del usuario


# ---------- PRODUTO ----------

def cadastrar_produto(nome, marca, data, quantidade, preco):
    try:
        produto = Produto()
        produto.cadastrar(nome=nome, marca=marca, data=data, quantidade=quantidade, preco=preco)
        return "Produto cadastrado com sucesso."
    except Exception as e:
        return f"Erro ao cadastrar produto: {e}"
    finally:
        del produto

def editar_produto(id, nome, marca, data, quantidade, preco):
    try:
        produto = Produto()
        produto.editar(id, nome=nome, marca=marca, data=data, quantidade=quantidade, preco=preco)
        return "Produto editado com sucesso."
    except Exception as e:
        return f"Erro ao editar produto: {e}"
    finally:
        del produto

def deletar_produto(id):
    try:
        produto = Produto()
        produto.deletar(id)
    except Exception as e:
        print(f"Erro ao excluir produto: {e}")
    finally:
        del produto

def listar_produto():
    try:
        produto = Produto()
        produto.cursor.execute(f"SELECT * FROM {produto.nome_tabela}")
        registros = produto.cursor.fetchall()
        return registros
    except Exception as e:
        print(f"Erro ao listar produtos: {e}")
        return []
    finally:
        del produto