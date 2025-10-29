#Criamos no decorador app_joao com página dinâmica
from flask import Flask, render_template

app_joao = Flask(__name__)
 

@app_joao.route("/")  
def homepage():     
    return render_template ("homepage.html")

@app_joao.route("/index")
def indice():
    return render_template ("index.html") 

@app_joao.route("/contato")
def contato():
    return render_template("contato.html") 

@app_joao.route("/usuario")
def dados_usuario():

    dados_usu = {"nome": "João","profissao": "Estudante", "disciplina":"Desenvolvimento Web III"}
    return render_template("usuario.html",  dados = dados_usu)
                                          




@app_joao.route('/usuario/<id>')
def saudacao(id):
    
    return render_template('homepage_nome.html', nome=id)

@app_joao.route("/usuario/<nome_usuario>;<nome_profissao>;<nome_disciplina>") 

def usuario (nome_usuario, nome_profissao, nome_disciplina): 
    
    dados_usu = {"profissao": nome_profissao, "disciplina": nome_disciplina}

    return render_template ("usuario.html", nome=nome_usuario, dados = dados_usu)  


if __name__ == "__main__": 
     app_joao.run(port = 8000) 