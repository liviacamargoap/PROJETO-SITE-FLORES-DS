from flask  import Flask,render_template


app = Flask(__name__)


# Pagina inicial
@app.route("/inicial")
def pagina_incial():
    return render_template ("inicial.html")

@app.route("/compras")
def pagina_compras():
    return render_template ("compras.html")

app.run(debug=True)    