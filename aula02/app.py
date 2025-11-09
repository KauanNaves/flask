from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # ROTA PRINCIPAL
def home():
    nome = "Kauan Augusto Naves"
    linguagens = ["Python", "JavaScript", "C", "HTML", "CSS"]
    return render_template('home.html', nome=nome, linguagens=linguagens)
    

if __name__ == "__main__":
    app.run(debug=True)
    