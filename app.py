from flask import Flask, render_template, redirect, session
from model.produtos_controler import Produtos

app = Flask(__name__)

app.secret_key = "key"

@app.route("/")
def pagina_inicial():
    return render_template("inicial.html")

@app.route("/logar")
def logar():
    # session = uma lista | guardar informações do usuario
    # criou uma lista "usuario" para guardar as listas (organizar)
    session["nome"] = "Usuário"
    session["foto"] = "https://img.freepik.com/fotos-premium/foto-de-grande-angular-de-uma-unica-arvore-crescendo-sob-um-ceu-nublado-durante-um-por-do-sol-cercado-por-grama_181624-22807.jpg?semt=ais_hybrid&w=740"
    return redirect("/")

@app.route("/deslogar")
def deslogar():
    session.clear()
    return redirect("/")

@app.route("/cadastro")
def pagina_cadastro():
    return render_template("cadastro.html")




# ajuda alex Filtro
# ve a categoria selecionada e direciona pro sql (cod no controller)
@app.route("/categoria/<filtro>")
def pagina_produto(filtro):
    lista_produtos = Produtos.obter_produtos(filtro)
    return render_template("produtos.html", lista_produtos_html = lista_produtos) 

@app.route("/categoria/todos")
def pagina_produtos():
    lista_produtos = Produtos.obter_todos_produtos()
    return render_template("produtos.html", lista_produtos_html = lista_produtos) 







@app.route("/compras")
def pagina_compra():
    return render_template("compras.html")




app.run(debug = True)