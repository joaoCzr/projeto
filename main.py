from flask import Flask, render_template

app_joao = Flask(__name__, template_folder='templates')

@app_joao.route("/")  
def homepage():          
    return render_template("homepage.html")

@app_joao.route("/contato")
def contato():
    return render_template("contato.html") 

@app_joao.route("/index")
def indice():
    dados_usu = {"nome": "João"}
    return render_template("index.html", **dados_usu)

@app_joao.route("/usuario")
def dados_usuario():
    dados_usu = {"nome": "João", "profissao": "Estudante", "disciplina":"Desenvolvimento Web III"}
    return render_template("usuario.html", dados=dados_usu)

if __name__ == "__main__":
    app_joao.run(port=8000, debug=True)