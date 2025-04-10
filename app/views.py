from flask import Blueprint, render_template, request
from controlles import cadastrar_usuario

app= Blueprint('app', __name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/cadastro', methods=['GET', 'POST'])

def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        mensagem = cadastrar_usuario(nome, email, senha)
        return render_template ('cadastro.html',mensagem=mensagem)
    
    return render_template('cadastro.html')

