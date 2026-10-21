Resumo das Atividades da Aula - Projeto com Flask

O que eu fiz neste projeto:

- Preparação do ambiente: Instalei o gerenciador de pacotes 'uv' via PowerShell e depois usei o terminal para inicializar o projeto e instalar o Flask.
Comandos utilizados:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.13.4/install.ps1 | iex"
uv init
uv add Flask

- Criação do Servidor e Rotas (app.py): Configurei o arquivo principal da aplicação. Criei rotas básicas, rotas usando parâmetros de URL e rotas dinâmicas.
Código do app.py:

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

- HTML Dinâmico (Jinja2): Dentro da pasta 'templates', criei o 'ola.html'. ({% if nome %}) para a página exibir uma saudação personalizada ou o padrão "Olá, Flask!".
Código do templates/ola.html:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Olá do Flask</title>
</head>
<body>
    {% if nome %}
        <h1>Olá, {{ nome }}!</h1>
    {% else %}
        <h1>Olá, Flask!</h1>
    {% endif %}
</body>
</html>

Comando para rodar:
uv run flask run
