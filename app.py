from flask import Flask, render_template, redirect, session
from model.produtos_controler import Produtos
from model.user_controler import Usuario

app = Flask(__name__)

app.secret_key = "key"

@app.route("/")
def pagina_inicial():
    return render_template("inicial2.html")

# LOGIN E CADASTRO
@app.route("/login")
def login():
    fazer_login = Usuario.login()
    # session = uma lista | guardar informações do usuario
    # criou uma lista "usuario" para guardar as listas (organizar)
    session["nome"] = "Usuário"
    session["foto"] = "https://img.freepik.com/fotos-premium/foto-de-grande-angular-de-uma-unica-arvore-crescendo-sob-um-ceu-nublado-durante-um-por-do-sol-cercado-por-grama_181624-22807.jpg?semt=ais_hybrid&w=740"
    return redirect(fazer_login, "/")

@app.route("/pagina/login")
def pagina_login():
    return render_template("login.html")

@app.route("/logoff")
def logoff():
    session.clear()
    return redirect("/")

@app.route("/cadastro")
def cadastro():
    fazer_cadastro = Usuario.cadastrar()
    return redirect(fazer_cadastro, "/pagina/login")



# CATEGORIAS PRODUTOS
# ajuda alex Filtro
# ve a categoria selecionada e direciona pro sql (cod no controller)
@app.route("/categoria/<filtro>")
def pagina_produto(filtro):
    lista_produtos = Produtos.obter_produtos(filtro)
    return render_template("inicial2.html", lista_produtos_html = lista_produtos) 

@app.route("/categoria/todos")
def pagina_produtos():
    lista_todos_produtos = Produtos.obter_todos_produtos()
    return render_template("inicial2.html", lista_todos_produtos_html = lista_todos_produtos) 

@app.route("/categorias")
def categorias():
    lista_categorias = Produtos.obter_categorias()
    return render_template("inicial2.html", lista_categorias_html = lista_categorias)






# CARRINHO DETALHES
@app.route("/carrinho")
def pagina_compra():
    return render_template("carrinho.html")

@app.route("/detalhes")
def pagina_detalhes():
    return render_template("detalhes-produto.html")




app.run(debug = True)