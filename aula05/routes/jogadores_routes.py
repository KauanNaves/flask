from flask import Blueprint, render_template, request
from criar_banco import *

jogadores_routes = Blueprint('jogadores', __name__)

@jogadores_routes.route('/jogadores')
def listar_jogadores():
    jogadores = listar_jogadores_do_banco()
    return render_template('jogadores.html', jogadores=jogadores)

@jogadores_routes.route('/jogadores/adicionar-jogador', methods=['GET'])
def adicionar_jogador():
    return render_template('adicionar_jogador.html')

@jogadores_routes.route('/jogadores/adicionar-jogador', methods=['POST'])
def salvar_jogador():
    nome = request.form['nome']
    idade = request.form['idade']
    posicao = request.form['posicao']
    time = request.form['time']
    adicionar_jogador_ao_banco(nome, idade, posicao, time)
    return render_template('sucesso.html') 

@jogadores_routes.route('/jogadores/excluir-jogador/<int:id>', methods=['POST'])
def excluir_jogador(id):
    excluir_jogador_do_banco(id)
    return render_template('sucesso.html', excluir=True)

@jogadores_routes.route('/jogadores/editar-jogador/<int:id>', methods=['GET', 'POST'])
def editar_jogador(id):
    if request.method == 'GET':
        jogador = listar_jogador_por_id(id)
        return render_template('editar_jogador.html', jogador=jogador)
    else:
        nome = request.form['nome']
        idade = request.form['idade']
        posicao = request.form['posicao']
        time = request.form['time']
        editar_jogador_no_banco(id, nome, idade, posicao, time)
        return render_template('sucesso.html', editar=True)