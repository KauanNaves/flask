from flask import Flask, render_template, request

app = Flask(__name__)

# Definindo rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Definindo rota GET do formulário
@app.route("/form")
def form():
    return render_template('form.html')

# Definindo a rota PUT do formulário
@app.route('/resultado', methods=['POST'])
def resultado():
    nome = request.form['input-nome']
    return render_template('resultado.html', nome=nome)

# @app.route('/resultado')
# def resultado():
#     return render_template('resultado.html')









if __name__ == "__main__":
    app.run(debug=True)
