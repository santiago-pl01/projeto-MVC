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

#------------------------------------------------------
# TESTE
#------------------------------------------------------

if __name__ == "__main__":
   '''print("📌 Testando cadastro de usuário:")
    msg = cadastrar_usuario("maria", "maria@email.com", "0987")
    print("Resultado:", msg)

    print("\n📌 Lista de usuários:")
    print(cliente_model.listar())
  

    print("\n📌 Testando cadastro de produto:")
    m = cadastrar_produto("Agenda Verde", "Tilibra", "20250410", 3)
    print("Resultado:", m)

    print("\n📌 Lista de produtos:")
    print(produto_model.listar())

print("\n📌 Lista completa antes de editar/deletar:")
usuarios = cliente_model.listar()
print(usuarios)

# Pegue o primeiro ID da lista para usar nos testes:
if usuarios:
    id_existente = usuarios[0][0]

    print("\n📌 Testando editar com ID existente:")
    print(editar_usuario(id_existente, "Nome Teste", "email@email.com", "1293"))

    print("\n📌 Testando deletar com ID existente:")
    print(deletar_usuario(id_existente))
else:
    print("⚠ Nenhum usuário cadastrado para testar editar/deletar.")

    print("\n📌 Lista de produtos antes de editar/deletar:")
produtos = listar_produto()
print(produtos)

# Testar com produto real, se houver
if produtos:
    id_existente = produtos[0][0]

    print("\n📌 Testando edição de produto com ID existente:")
    print(editar_produto(id_existente, "Produto Editado", "Nova Marca", "20250505", 10))

    print("\n📌 Testando exclusão de produto com ID existente:")
    print(deletar_produto(id_existente))
else:
    print("⚠ Nenhum produto cadastrado para testar editar/deletar.")

# Teste com ID que provavelmente não existe
print("\n📌 Testando edição de produto com ID inexistente:")
print(editar_produto(9999, "X", "Y", "20000101", 1))

print("\n📌 Testando exclusão de produto com ID inexistente:")
print(deletar_produto(9999))'''
'''if __name__ == "__main__":
    # ... (seus testes anteriores de cadastro/listagem aqui) ...

    print("\n=== TESTES DE EDIÇÃO E DELEÇÃO ===")

    # Pega o primeiro usuário e produto da lista para testes
    cliente= listar_cliente()
    produtos = listar_produto()

    # ---- TESTE COM USUÁRIO ---- #
    if cliente and len(cliente) > 0:
        id_usuario = cliente[2][2]  # Pega o ID do primeiro usuário
        print(f"\n📌 Editando usuário (ID: {id_usuario}):")
        resultado_edicao = editar_usuario(
            id_usuario, 
            "Novo Nome", 
            "novoemail@teste.com", 
            "novasenha123"
        )
        print("Resultado:", resultado_edicao)

        print(f"\n📌 Deletando usuário (ID: {id_usuario}):")
        resultado_delecao = deletar_usuario(id_usuario)
        print("Resultado:", resultado_delecao)

        # Verifica se realmente foi deletado
        print("\n📌 Verificando se usuário foi removido:")
        if not cliente_model.existe(id_usuario):
            print("✅ Usuário deletado com sucesso!")
        else:
            print("❌ Falha: Usuário ainda existe no banco!")
    else:
        print("\n⚠ Nenhum usuário cadastrado para testar edição/deleção")

    # ---- TESTE COM PRODUTO ---- #
    if produtos and len(produtos) > 0:
        id_produto = produtos[0][0]  # Pega o ID do primeiro produto
        print(f"\n📌 Editando produto (ID: {id_produto}):")
        resultado_edicao = editar_produto(
            id_produto,
            "Produto Editado", 
            "Marca Nova", 
            "20250101", 
            100
        )
        print("Resultado:", resultado_edicao)

        print(f"\n📌 Deletando produto (ID: {id_produto}):")
        resultado_delecao = deletar_produto(id_produto)
        print("Resultado:", resultado_delecao)

        # Verifica se realmente foi deletado
        print("\n📌 Verificando se produto foi removido:")
        if not produto_model.existe(id_produto):
            print("✅ Produto deletado com sucesso!")
        else:
            print("❌ Falha: Produto ainda existe no banco!")
    else:
        print("\n⚠ Nenhum produto cadastrado para testar edição/deleção")

    # ---- TESTE COM ID INEXISTENTE (ERRO) ---- #
    print("\n=== TESTES COM ID INEXISTENTE ===")
    id_fake = 99999  # ID que não existe

    print(f"\n📌 Tentando editar usuário (ID fake: {id_fake}):")
    print(editar_usuario(id_fake, "Nome", "email@fake", "123"))  # Espera erro

    print(f"\n📌 Tentando deletar usuário (ID fake: {id_fake}):")
    print(deletar_usuario(id_fake))  # Espera erro

    print(f"\n📌 Tentando editar produto (ID fake: {id_fake}):")
    print(editar_produto(id_fake, "X", "Y", "20250101", 1))  # Espera erro

    print(f"\n📌 Tentando deletar produto (ID fake: {id_fake}):")
    print(deletar_produto(id_fake))  # Espera erro'''

if __name__ == "__main__":
    print("📌 Testando cadastro duplicado:")

    # Cadastra um usuário pela primeira vez
    cadastrar_usuario("Maria", "maria@email.com", "123456")  # ✅ Sucesso

    # Tenta cadastrar o mesmo e-mail novamente


    # Cadastra um produto pela primeira vez
    print(cadastrar_produto("Caderno", "Tilibra", "20250101", 50))  # ✅ Sucesso

    # Tenta cadastrar o mesmo produto+marca novamente


    print(cliente_model.listar)
    print(produto_model.listar)