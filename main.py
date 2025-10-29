from flask import Flask, render_template
from flask import request  

app_joao = Flask(__name__, template_folder='t_templates') 

@app_joao.route("/") 
@app_joao.route("/index")  
def indice():
    return render_template ("t_index.html")                                               #optei por prefixar com t_ os nomes dos arquivos que usam template

@app_joao.route("/contato")
def contato():
    return render_template("t_contato.html") 


@app_joao.route("/usuarios/<nome_usuario>;<nome_profissao>")

@app_joao.route("/usuarios", defaults={"nome_usuario":"usuário?","nome_profissao":""})  
def usuarios (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Desenvolvimento Web III"}
    return render_template ("t_usuario.html", nome=nome_usuario, dados = dados_usu)  


@app_joao.route("/login")
def login():
    return render_template("t_login.html") 


@app_joao.route("/autenticar", methods=['POST'] ) 
def autenticar():

    
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')
    return f"usuario: {usuario} e senha: {senha}"

if __name__ == "__main__": 
     app_joao.run(port = 8000) 
     