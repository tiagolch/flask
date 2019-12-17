from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


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

@app.route('/Ramais')
def ramal():
    return render_template('ramais.html', titulo='Listagem de Ramais', lista=lista)


@app.route('/novoRamal')
def novo_ramal():
    return render_template('novoRamal.html', titulo='Novo Ramal')


@app.route('/criar', methods = ['POST',])
def criar():
    empresa = request.form['empresa']
    setor = request.form['setor']
    nome = request.form['nome']
    ramal = request.form['ramal']
    ramais1 = Ramais(empresa, setor, nome, ramal)
    lista.append(ramais1)
    return render_template('ramais.html', titulo='Ramais', lista=lista)
    #return redirect('/')

app.run(debug=True)

