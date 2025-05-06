from flask import Blueprint, render_template,request
from controller import *

app= Blueprint('app', __name__)

@app.route('/')
def home():
    return render_template('index.html')


# rota do cadastro

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        mensagem = cadastrar_usuario(nome, email, senha)
        return render_template ('cadastro.html',mensagem=mensagem)
    
    return render_template('cadastro.html')
    


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

'''@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    # Lógica para editar o cliente com o id fornecido
    pass

@app.route('/excluir/<int:id>', methods=['GET'])
def excluir_cliente(id):
    # Lógica para excluir o cliente com o id fornecido
    pass'''
