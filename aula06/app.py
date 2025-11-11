from flask import Flask
from database.connection import create_table_notes
from routes.main_routes import main_routes
from routes.students_routes import studants_routes 

app = Flask(__name__) # Criando a aplicação Flask
create_table_notes() # Criando a tabela de notas no banco de dados / criando o banco de dados se não existir

# Registrando rotas dos blueprints
app.register_blueprint(main_routes)
app.register_blueprint(studants_routes)


if __name__ == '__main__': # Executando a aplicação Flask
    app.run(debug=True)