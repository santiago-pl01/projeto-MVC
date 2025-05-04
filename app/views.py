from flask import Blueprint, render_template,request
from controller import *

app= Blueprint('app', __name__)

@app.route('/')
def home():
    return render_template('index.html')


# rota do cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    mensagem = ""
    id_edicao = request.args.get('id')
    cliente_dados = None

    if request.method == 'POST':
        id_form = request.form.get('id')
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        if id_form:  # Editar
            cliente = Cliente()
            cliente.editar(int(id_form), nome=nome, email=email)
            mensagem = "Usuário editado com sucesso!"
        else:  # Cadastrar
            mensagem = cadastrar_usuario(nome, email, senha)

    if id_edicao:  # Preencher formulário para edição
        cliente = Cliente()
        cliente.cursor.execute("SELECT id, nome, email FROM usuarios WHERE id = ?", (id_edicao,))
        resultado = cliente.cursor.fetchone()
        if resultado:
            cliente_dados = {"id": resultado[0], "nome": resultado[1], "email": resultado[2]}

    clientes = Cliente().listar()
    return render_template("cadastro.html", mensagem=mensagem, clientes=clientes, cliente_dados=cliente_dados)


@app.route('/produto', methods=['GET', 'POST'])
def page():
    if request.method == 'POST':
        nome = request.form.get('nome')
        marca = request.form.get('marca')
        data = request.form.get('data')
        quantidade = request.form.get('quantidade')

        mensagem = cadastrar_produto(nome, marca, data, quantidade)
        return render_template('produto.html', mensagem=mensagem)

    return render_template('produto.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    # Lógica para editar o cliente com o id fornecido
    pass

@app.route('/excluir/<int:id>', methods=['GET'])
def excluir_cliente(id):
    # Lógica para excluir o cliente com o id fornecido
    pass
