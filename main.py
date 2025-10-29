from flask import Flask  

app_Joao = Flask(__name__)
@app_Joao.route('/Ola')  

def raiz():
    return 'Olá, turma!'

def saudacoes(nome):
    return f'Olá, {nome}!'

if __name__ == "__main__":  
   
    app_Joao.run()  
