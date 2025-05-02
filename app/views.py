from flask import Blueprint, render_template,request
from controller import cadastrar_usuario

app= Blueprint('app', __name__)

@app.route('/')
def home():
    return render_template('index.html')


# rota do cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        mensagem = cadastrar_usuario(nome, email, senha)
        return render_template ('cadastro.html',mensagem=mensagem)
    
    return render_template('cadastro.html')

@app.route('/produto')
def page():
    return render_template('produto.html')