from flask import Blueprint, render_template,request
import controller

app= Blueprint('app', __name__)

@app.route('/')
def home():
    return render_template('index.html')

#get(codigo para a tela)
#post(tela para)

# rota do cadastro

#cadastro do usuario
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_cliente():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        mensagem = controller.cadastrar_usuario(nome, email, senha)
        return render_template ('cadastro.html',mensagem=mensagem)
    
    return render_template('cadastro.html')
    

#cadastro do produto
@app.route('/produto', methods=['GET','POST'])
def cadastro_produto():

    if request.method == 'POST':
        nome = request.form.get('nome')
        marca = request.form.get('marca')
        data = request.form.get('data')
        quantidade =int(request.form.get('quantidade'))
        preco= int(request.form.get('preco'))

        mensagem = controller.cadastrar_produto(nome, marca, data, quantidade,preco)
        return render_template('produto.html', mensagem=mensagem)

    return render_template('produto.html')

@app.route('/editar_usuario/<int:id>', methods=['GET','POST'])
def editar_usuario():

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        mensagem = controller.cadastrar_usuario(nome, email, senha)
        return render_template ('cadastro.html',mensagem=mensagem)
    
    return render_template, ('cadastro.html')
#excluir usuario
@app.route('/excluir_usuario/<int:id>', methods=['GET'])
def excluir_usuario(id):
    controller.deletar_usuario(id)
    return render_template('cadastro.html')

#xcluir produto
@app.route('/excluir/<int:id>', methods=['GET'])
def excluir_produto(id):
    controller.deletar_produto(id)
    return render_template('produto.html')

#editar produto
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_produto():

    if request.method == 'POST':
        nome = request.form.get('nome')
        marca = request.form.get('marca')
        data = request.form.get('data')
        quantidade =int(request.form.get('quantidade'))
        preco= int(request.form.get('preco'))

        mensagem = controller.cadastrar_produto(nome, marca, data, quantidade,preco)
        return render_template('produto.html', mensagem=mensagem)

    return render_template('cadastro.html')
