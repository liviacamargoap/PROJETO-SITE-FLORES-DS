from flask import Flask, render_template, redirect, session

app = Flask(__name__)

app.secret_key = "banana"

@app.route("/")
def pagina_inicial():
    return render_template("inicial.html")

@app.route("/logar")
def logar():
    # session = uma lista | guardar informações do usuario
    # criou uma lista "usuario" para guardar as listas (organizar)
    session["nome"] = "Godofredo"
    session["foto"] = "https://img.freepik.com/fotos-premium/foto-de-grande-angular-de-uma-unica-arvore-crescendo-sob-um-ceu-nublado-durante-um-por-do-sol-cercado-por-grama_181624-22807.jpg?semt=ais_hybrid&w=740"
    return redirect("/")

@app.route("/deslogar")
def deslogar():
    session.clear()
    return redirect("/")

app.run(debug = True)