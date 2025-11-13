from flask import Blueprint, render_template, request, url_for, redirect, flash, session
from database.connection import email_exists, add_user, get_user_by_email
from datetime import date
from werkzeug.security import check_password_hash, generate_password_hash

auth_routes = Blueprint('auth', __name__, url_prefix='/auth')

# Rotas principais
@auth_routes.route('/register', methods=["GET"])
def register():
    return render_template('register.html')

@auth_routes.route('/login', methods=["GET"])
def login():
    return render_template('login.html')

@auth_routes.route('/forgot', methods=['GET'])
def forgot():
    return render_template('forgot_password.html')

# Rotas para logar/registrar usuário
@auth_routes.route('/register', methods=['POST'])
def register_user():
    # Pegando dados do formulário
    name = request.form.get('name-user').lower().strip()
    email = request.form.get('email-user').strip()
    if not request.form.get('password-user') == request.form.get('confirm-password'):
        flash('DIGITE SENHAS IGUAIS!')
        return redirect(url_for('auth.register'))
    password = generate_password_hash(request.form.get('password-user'))
    date_created = date.today() #2025-11-12
    exists_email = email_exists(email)
    if not exists_email:
        add_user(name, email, password, date_created)
        flash('USUÁRIO CADASTRADO COM SUCESSO! <br> REALIZE O LOGIN!', category='message')
        return redirect(url_for('auth.login'))
    
    flash('ESTE USUÁRIO JÁ ESTÁ CADASTRADO! TENTE NOVAMENTE COM OUTROS DADOS!', category='message')
    return redirect(url_for('auth.register'))

@auth_routes.route('/login', methods=['POST'])
def user_login():
    email = request.form.get('email-user-login')
    data_user = get_user_by_email(email)
    if not data_user:
        flash('ESTE USUÁRIO NÃO EXISTE!')
        return redirect(url_for('auth.login'))
    password = request.form.get('password-user-login')
    if not check_password_hash(data_user['password'], password):
        flash('USUÁRIO OU SENHA INCORRETA!')
        return redirect(url_for('auth.login'))
    session['user_id'] = data_user['id']
    flash(f'SEJA BEM-VINDO, {data_user['name'].title()}!')
    return redirect(url_for('properties.home_properties'))


@auth_routes.route('/forgot', methods=['POST'])
def forgot_password():
    pass
