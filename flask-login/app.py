from flask import Flask
from routes.main_routes import main_routes
from routes.auth_routes import auth_routes
from routes.property_routes import properties_routes
from database.connection import create_all_tables
import os

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY', 'chave-secreta-do-IMOB_GESTOR')

app.register_blueprint(main_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(properties_routes)



if __name__ == '__main__':
    create_all_tables()
    app.run(debug=True)
