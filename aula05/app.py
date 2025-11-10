from flask import Flask
from routes.main_routes import main_routes
from routes.jogadores_routes import jogadores_routes

app = Flask(__name__)

app.register_blueprint(main_routes)

app.register_blueprint(jogadores_routes)

if __name__ == '__main__':
    app.run(debug=True)
     