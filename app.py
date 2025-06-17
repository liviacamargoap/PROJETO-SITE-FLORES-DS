from flask import Flask, render_template, redirect, session, request
from model.produtos_controler import Produtos
from model.user_controler import Usuario

app = Flask(__name__)

app.secret_key = "key"

@app.route("/")
def pagina_inicial():
    produtos = Produtos.obter_todos_produtos()
    categorias = Produtos.obter_categorias()

    return render_template("inicial2.html", categorias = categorias, lista_produtos_html = produtos)

# LOGIN E CADASTRO
@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    login_sucesso = Usuario.login(usuario, senha) 

    if login_sucesso: 
        return redirect("/")
    else:
        return redirect("/pagina/login")

@app.route("/pagina/login")
def pagina_login():
    return render_template("login.html")

@app.route("/logoff")
def logoff():
    session.clear()
    return redirect("/")

@app.route("/cadastro", methods = ["post"])
def cadastro():
    
    usuario = request.form.get("usuario")
    telefone = request.form.get("telefone")
    endereco = request.form.get("endereco")
    senha = request.form.get("senha")
    Usuario.cadastrar(usuario, telefone, endereco, senha)
    return redirect("/pagina/login")

@app.route("/pagina/cadastro")
def pagina_cadastro():
    return render_template("cadastro.html")


# CATEGORIAS PRODUTOS
# ajuda alex Filtro
# ve a categoria selecionada e direciona pro sql (cod no controller)
@app.route("/categoria/<filtro>")
def pagina_produto(filtro):
    lista_produtos = Produtos.obter_produtos(filtro)
    categorias = Produtos.obter_categorias() 
    return render_template("categorias.html", lista_produtos_html=lista_produtos, categorias=categorias)

@app.route("/categoria/todos")
def pagina_todos_produtos(): 
    lista_todos_produtos = Produtos.obter_todos_produtos()
    categorias = Produtos.obter_categorias() 
    return render_template("inicial2.html", lista_produtos_html=lista_todos_produtos, categorias=categorias) 

# @app.route("/categorias")
# def categorias():
#     lista_categorias = Produtos.obter_categorias()
#     return render_template("inicial2.html", lista_categorias_html = lista_categorias)






# CARRINHO DETALHES
@app.route("/carrinho")
def pagina_compra():
    return render_template("carrinho.html")

@app.route("/detalhes")
def pagina_detalhes():
    return render_template("detalhes-produto.html")




app.run(debug = True)