from flask import Flask, render_template, request
from markupsafe import escape
 
app = Flask(__name__)
 
@app.route("/")
def ola_mundo():
    return '<p>Olá, Mundo!</p>'
 
@app.route("/pessoa")
def ola_palandi():
    nome = request.args.get("nome", "Flask")
    return f'<h1>Olá, {escape(nome)}</h1>'
 
@app.route("/usuario/<username>")
def home_usuario(username):
    return f'<p>Usuário: {escape(username)}</p>'
 
@app.route("/ola/")
@app.route("/ola/<nome>")
def ola_nome(nome = None):
    return render_template('ola.html', nome=nome)