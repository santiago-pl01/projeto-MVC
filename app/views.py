from flask import Blueprint, render_template,request
import controller

app= Blueprint('app',__name__)

@app.route('/')
def home():
    return render_template('index.html')

#get(codigo para a tela)
#post(tela para)

# rota do cadastro
#usuario--------------------------------------------------------------------------------------------------------

#cadastro do usuario
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_usuario():
    lista_usuario = controller.listar_usuario()
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        mensagem = controller.cadastrar_usuario(nome, email, senha)
        return render_template ('cadastro.html',mensagem=mensagem, usuarios = lista_usuario)
    
    
    return render_template('cadastro.html', usuarios = lista_usuario)


#editar usuario
@app.route('/editar_usuario/<int:id>', methods=['GET','POST'])
def editar_usuario(id):
    lista_usuario = controller.listar_usuario()
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        mensagem = controller.editar_usuario(id,nome, email, senha)
        return render_template ('cadastro.html',mensagem=mensagem, usuarios = lista_usuario)
    
    return render_template('cadastro.html', usuarios = lista_usuario)



#excluir usuario
@app.route('/excluir_usuario/<int:id>', methods=['GET', 'POST'])
def excluir_usuario(id):
    controller.deletar_usuario(id)
    lista_usuario = controller.listar_usuario()
    return render_template('cadastro.html', usuarios = lista_usuario)


#listar usuario
@app.route('/listar_usuario', methods=['GET', 'POST'])
def listar_usuario():
    lista_de_usuario = controller.listar_usuario()
    return render_template('cadastro.html', usuarios = lista_de_usuario)



#produto-------------------------------------------------------------------------------------------------------

#cadastro do produto
@app.route('/produto', methods=['GET','POST'])
def cadastro_produto():
    lista_produto = controller.listar_produto()
    if request.method == 'POST':
        nome = request.form.get('nome')
        marca = request.form.get('marca')
        data = request.form.get('data')
        quantidade =int(request.form.get('quantidade'))
        preco= int(request.form.get('preco'))

        mensagem = controller.cadastrar_produto(nome, marca, data, quantidade,preco)
        return render_template('produto.html', mensagem=mensagem, produtos = lista_produto)
        
    
    return render_template('produto.html', produtos= lista_produto)

#listar produto
@app.route('/listar_produto', methods=['GET', 'POST'])
def listar_produto():
    lista_de_produto= controller.listar_produto()
    return render_template('produto.html', produtos = lista_de_produto)

#xcluir produto
@app.route('/excluir/<int:id>', methods=['GET', 'POST'])
def excluir_produto(id):
    controller.deletar_produto(id)
    lista_de_produto= controller.listar_produto()
    return render_template('produto.html', produtos = lista_de_produto)

#editar produto
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
   
    if request.method == 'POST':
        nome = request.form.get('nome')
        marca = request.form.get('marca')
        data = request.form.get('data')
        quantidade =int(request.form.get('quantidade'))
        preco= int(request.form.get('preco'))

        mensagem = controller.editar_produto(id,nome, marca, data, quantidade,preco)
        listar_produto= controller.listar_produto()
        return render_template('produto.html', mensagem=mensagem, produtos= listar_produto)
    
    listar_produto= controller.listar_produto()
    return render_template('cadastro.html')