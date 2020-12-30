from flask import Flask
from calculadora import *

app = Flask(__name__)

@app.route('/')
def index():
    h1 = '<h1> Calculadora Olist </h1>'
    ol = '''
            <ol> 
                <li><a href='/soma'>Somar</a></li>
                <li><a href='/subtracao'>Subtrair</a></li>
                <li><a href='/multiplicacao'>Multiplicacao</a></li>
                <li><a href='/divisao'>divisao</a></li>
            </ol>
        '''
    return f'{h1} {ol}'

@app.route('/soma')
def somar():
    n1 = 3.0
    n2 = 5.0
    resultado = soma(n1, n2)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> A soma de 3+5 é : {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'


@app.route('/subtracao')
def subtra():
    n1 = 3.0
    n2 = 5.0
    resultado = subtracao(n1, n2)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> A subtracao de 3-5 é : {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'

@app.route('/multiplicacao')
def multi():
    n1 = 3.0
    n2 = 5.0
    resultado = multiplicacao(n1, n2)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> A multiplicacao de 3*5 é : {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'

@app.route('/divisao')
def divi():
    n1 = 3.0
    n2 = 5.0
    resultado = divisao(n1, n2)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> A divisao de 3:5 é : {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'

app.run()

