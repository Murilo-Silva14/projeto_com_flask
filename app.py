from flask import Flask, render
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return '<p>Olá, Mundo!</p>'

@app.route("/pessoa")
def ola_pessoa():
    nome = request.args.get("nome", "Flask")
    return f'<h1>Olá, {escape(nome)}</h1>'

@app.route("/usuario/<username>")
def home_usuario(username):
    return f'<p>Usuário: {escape(username)}</p>'

@app.route.route("/ola")