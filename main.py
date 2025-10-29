from flask import Flask, render_template

app_joao = Flask(__name__ , template_folder= 'templates')


@app_joao.route("/") 
def homepage():          
    return render_template ("homepage.html")

@app_joao.route("/contato")
def contato():
    return render_template("contato.html") 

if __name__ == "__main__":
     app_joao.run(port = 8000)
                                