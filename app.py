# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, User
import re
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'troque-esta-chave-por-uma-segura'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Regex de requisitos: min 6 chars, 1 upper, 1 digit, 1 special char
PASSWORD_REGEX = re.compile(
    r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_\-+=\[{\]};:\'",<.>/?\\|`~]).{6,}$'
)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email','').strip()
        senha = request.form.get('senha','')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(senha):
            session['user_id'] = user.id
            session['user_nome'] = user.nome
            return redirect(url_for('dashboard'))
        else:
            flash('Email ou senha incorretos.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        nome = request.form.get('nome','').strip()
        cpf = request.form.get('cpf','').strip()
        email = request.form.get('email','').strip()
        telefone = request.form.get('telefone','').strip()
        endereco = request.form.get('endereco','').strip()
        senha = request.form.get('senha','')
        senha_conf = request.form.get('senha_conf','')

        # validação servidor: senha e confirmação iguais
        if senha != senha_conf:
            flash('Senha e confirmação não coincidem.', 'danger')
            return redirect(url_for('register'))

        # validação dos requisitos
        if not PASSWORD_REGEX.match(senha):
            flash('Senha não atende aos requisitos mínimos.', 'danger')
            return redirect(url_for('register'))

        # checar duplicatas
        if User.query.filter((User.email==email)|(User.cpf==cpf)).first():
            flash('Email ou CPF já cadastrado.', 'danger')
            return redirect(url_for('register'))

        user = User(nome=nome, cpf=cpf, email=email, telefone=telefone, endereco=endereco)
        user.set_password(senha)
        db.session.add(user)
        db.session.commit()
        flash('Cadastro realizado com sucesso. Faça login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', nome=session.get('user_nome'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
