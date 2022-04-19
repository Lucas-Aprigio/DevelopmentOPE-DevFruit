from flask import Flask
from flask import render_template
import os

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/cadastro.html')
def cadastro():
    return render_template('cadastro.html')

@app.route('/finalizar.html')
def finalizar():
    return render_template('finalizar.html')

@app.route('/login.html')
def login():
    return render_template('login.html')


@app.route('/pagamento')
def pagamento():
    return render_template('pagamento.html')

@app.route('/sair')
def sair():
    return render_template('sair.html')
    
@app.route('/sobre.html')
def sobre():
    return render_template('sobre.html')

    
@app.route('/endereco.html')
def endereco():
    return render_template('endereco.html')

if __name__=='main':
    app.run(debug=True,host='0.0.0.0',port=5000)

