from flask import Blueprint, render_template

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
    pass

@auth_routes.route('/login', methods=['POST'])
def user_login():
    pass

@auth_routes.route('/forgot', methods=['POST'])
def forgot_password():
    pass
