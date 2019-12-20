from flask import Flask, render_template, request, redirect, session, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'alura'


class Ramais:
    def __init__(self, empresa, setor, nome, ramal):
        self.empresa = empresa
        self.setor = setor
        self.nome = nome
        self.ramal = ramal


r1 = Ramais('Artlatex', 'CPD', 'Tiago', '3730')
r2 = Ramais('Artlatex', 'CPD', 'Cristian', '3659')
r3 = Ramais('Artlatex', 'CPD', 'Emerson', '3688')
lista = [r1, r2, r3]

@app.route('/ramais')
def ramal():
    return render_template('ramais.html', titulo='Listagem de Ramais', lista=lista)


@app.route('/novoRamal')
def novo_ramal():
    return render_template('novoRamal.html', titulo='Novo Ramal')


@app.route('/criar', methods=['POST',])
def criar():
    empresa = request.form['empresa']
    setor = request.form['setor']
    nome = request.form['nome']
    ramal = request.form['ramal']
    ramais1 = Ramais(empresa, setor, nome, ramal)
    lista.append(ramais1)
    #return render_template('ramais.html', titulo='Ramais', lista=lista)
    return redirect('/ramais')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario']+' Logou com Sucesso!')
        return redirect('/ramais')
    else:
        flash('Não logado, tente novamente!' )
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuario deslogado!')
    return redirect('/ramais')

app.run(debug=True)

