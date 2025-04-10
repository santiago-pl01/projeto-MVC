from model import Cliente

cliente_model = Cliente()

def cadastrar_usuario(nome, email, senha):
    if not nome or not email or not senha:
        return "Preencha todos os campos"
    
    cliente_model.cadastrar_cliente(nome, email, senha)
    return "Usuário cadrastrado com sucesso!"

def listar_usuarios():
    return cliente_model.listar_cliente()