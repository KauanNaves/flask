from flask import Flask, render_template, request

app = Flask(__name__)

# A rota principal que exibe o formulário
@app.route('/')
def formulario():
    return render_template('form.html')

# A rota que processa o formulário e exibe a mensagem de boas-vindas
@app.route('/resultado', methods=["POST"])
def resultado():
    nome = request.form['nome']
    return render_template('resultado.html', nome=nome)



if __name__ == '__main__':
    app.run(debug=True)