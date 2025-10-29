

from flask import Flask 

app_joao = Flask(__name__)  


@app_joao.route('/Ola')  


def raiz():
    return 'Olá, professora!'

if __name__ == "__main__": 
    app_joao.run()  
