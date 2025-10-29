from flask import Flask

joao_app = Flask(__name__)

@joao_app.route("/")
def home():
    return "Olá, este é o primeiro teste da framework!!"


joao_app.run()