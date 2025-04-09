from flask import Blueprint, render_template

app= Blueprint('app', __name__)

@app.route('/')
#usar este  para referenciar
def home():
    return render_template('index.html')

@app.route('/pagina2')
def homepage():
    return render_template('pagina2.html')

#ao apertar o botão cadastrar em HTML, o views serve como uma rota, ele vai direcionar a acão cadastrar as regras de negocio como ver se os campos
#verificar os dados, se eles estão corretos