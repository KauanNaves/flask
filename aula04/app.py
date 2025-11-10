from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') # Rota principal
def index():
    return render_template('index.html')

@app.route('/form') # Rota formulário
def form():
    return render_template('form.html')

@app.route('/resultado', methods=["POST"]) # Rota resultado-formulário
def resultado():
    nome = request.form['nome']
    time = request.form['time']
    return render_template('resultado.html', nome=nome, time=time)

if __name__ == '__main__':  
    app.run(debug=True)