# Iniciando meus estudos em Flask

from flask import Flask

# Criando a aplicação Flask
app = Flask(__name__)

# Definindo uma rota principal
@app.route("/") # Definindo a rota "/"
def home(): # Esta é a função que a rota "/" irá executar # Enviando uma resposta HTTP
    return '<h1>Olá, Flask!</h1>' \
        '<p>Este é o meu primero app usando o Flask!🚀</p>' \
        '<a target="_self" href="http://127.0.0.1:5000/about">Página Sobre Mim</a> <br>' \
        '<a target="_self" href="http://127.0.0.1:5000/contat">Página Contatos</a>' 

# Definindo uma rota adicional "/about"
@app.route("/about")
def about():
    return "<h1>Sobre mim</h1>" \
    "<p>Sou um desenvolvedor Python aprendendo Flask!</p>" \
    "<p>Voltar a página<a href='http://127.0.0.1:5000/'> Home</a></p>"

@app.route("/contat")
def contat():
    return '<h1>Contatos</h1>' \
    '<a target="_blank" href="https://kauannazanaves0@gmail.com">kauannazanaves0@gmail.com</a> <br>' \
    '<a target="_blank" href="https://github.com/KauanNaves">GitHub - Kauan Naves</a> <br>' \
    '<a target="_blank" href="https://www.linkedin.com/in/kauan-naves-a5a321276">Linkedin - Kauan Naves</a> <br>' \
    '<p>Voltar a página <a target="_self" href="http://127.0.0.1:5000/"> Home</a></p>'





if __name__ == "__main__":
    app.run(debug=True)
