from model import Cliente, Produto  # importa as classes

# cria instâncias para usar funções do model
cliente_model = Cliente()
produto_model = Produto()

#------------------------------------------------
# FUNÇÕES CLIENTE
#------------------------------------------------

def cadastrar_usuario(nome, email, senha): 
    if not nome or not email or not senha:
        return "Preencha todos os campos"
    cliente_model.cadastrar(nome=nome, email=email, senha=senha)
    return "Usuário cadastrado com sucesso!"

def listar_cliente():
    return cliente_model.listar()

def editar_usuario(id, nome, email, senha):
    if not nome or not email or not senha:
        return "Preencha todos os campos."
    
    if not cliente_model.existe( id):
        return "usuario nao encontrado"


    cliente_model.editar(id, nome=nome, email=email, senha=senha)
    return "Usuário editado com sucesso!"

def deletar_usuario(id):
    if not cliente_model.existe(id):
        return"usuario nao encontrado"
    
    cliente_model.deletar(id)
    return "Usuário deletado com sucesso!"

#------------------------------------------------------
# FUNÇÕES PRODUTO
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

    if not produto_model.existe( id):
        return "produto nao encontrado"
    
    produto_model.editar(id, nome=nome, marca=marca, data=data, quantidade=quantidade)
    return "Produto editado com sucesso!"

def deletar_produto(id):
    if not produto_model.existe( id):
        return "produto nao encontrado"

    produto_model.deletar(id)
    return "Produto deletado com sucesso!"

if __name__ == "__main__":

    # Teste rápido
    print("Cadastrando produto...")
    msg = cadastrar_produto("Caderno", "Tilibra", "2025-04-10", 50)
    print(msg)

    print("\nLista de produtos:")
    print(listar_produto)