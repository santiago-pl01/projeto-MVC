from model import Cliente, Produto

cliente_model = Cliente()
produto_model = Produto()

#------------------------------------------------
#FUNCOES CLIENTE
#------------------------------------------------

def cadastrar_usuario(nome, email, senha):
    if not nome or not email or not senha:
        return "Preencha todos os campos"
    
    cliente_model.cadastrar_cliente(nome, email, senha)
    return "Usuário cadrastrado com sucesso!"

def listar_usuarios():
    return cliente_model.listar_cliente()

def editar_usuario(id, nome, email, senha):
    if not nome or not email or not senha:
        return "Preencha todos os campos."
    cliente_model.editar(id, nome=nome, email=email, senha=senha)
    return "Usuário editado com sucesso!"

def deletar_usuario(id):
    cliente_model.deletar(id)
    return "Usuário deletado com sucesso!"

#------------------------------------------------------
#                  FUNCOES PRODUTO
#------------------------------------------------------

def cadastrar_produto(nome, marca, data, quantidade):
    if not nome or not marca or not data or not quantidade:
        return "Preencha todos os campos do produto"
    produto_model.cadastrar(nome=nome, marca=marca, data=data, quantidade=quantidade)
    return "Produto cadastrado com sucesso!"

def listar_produto():
    return produto_model.listar()

def editar_produto(id, nome, marca, data, quantidade):
    if not nome or not marca or not data or not quantidade:
        return "Preencha todos os campos para editar."
    produto_model.editar(id, nome=nome, marca=marca, data=data, quantidade=quantidade)
    return "Produto editado com sucesso!"

def deletar_produto(id):
    produto_model.deletar(id)
    return "Produto deletado com sucesso!"
    
