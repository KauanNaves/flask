import sqlite3

def conectar_ou_criar_banco():
    connection = sqlite3.connect('database.db')
    criar_tabela_jogadores(criar_cursor(connection))
    return connection

def desconectar_banco(connection, cursor):
    cursor.close()
    connection.close()

def criar_cursor(connection):
    return connection.cursor()

def criar_tabela_jogadores(cursor):
    cursor.execute('''
               CREATE TABLE IF NOT EXISTS jogadores (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER NOT NULL,
               posicao TEXT NOT NULL,
               time TEXT NOT NULL);
''')
    
def commitar_alteracoes(connection):
    connection.commit()

def adicionar_jogador_ao_banco(nome, idade, posicao, time):
    conn = conectar_ou_criar_banco()
    cursor = criar_cursor(conn)
    criar_tabela_jogadores(cursor)
    cursor.execute('''
        INSERT INTO jogadores (nome , idade, posicao, time)
                   VALUES (?, ?, ?, ?)''', (nome, idade, posicao, time))
    commitar_alteracoes(conn)
    desconectar_banco(conn, cursor)

def listar_jogadores_do_banco():
    conn = conectar_ou_criar_banco()
    cursor = criar_cursor(conn)
    criar_tabela_jogadores(cursor)
    cursor.execute('SELECT * FROM jogadores')
    jogadores = cursor.fetchall()
    jogadores_list = []
    for jogador in jogadores:
        dict_jogador = {
            'id': jogador[0],
            'nome': jogador[1],
            'idade': jogador[2],
            'posicao': jogador[3],
            'time': jogador[4]
        }
        jogadores_list.append(dict_jogador)
    desconectar_banco(conn, cursor)
    return jogadores_list

def excluir_jogador_do_banco(id):
    conn = conectar_ou_criar_banco()
    cursor = criar_cursor(conn)
    criar_tabela_jogadores(cursor)
    cursor.execute('DELETE FROM jogadores WHERE id = ?', (id,))
    commitar_alteracoes(conn)
    desconectar_banco(conn, cursor)

def listar_jogador_por_id(id):
    conn = conectar_ou_criar_banco()
    cursor = criar_cursor(conn)
    criar_tabela_jogadores(cursor)
    cursor.execute('SELECT * FROM jogadores WHERE id = ?', (id,))
    jogador = cursor.fetchone()
    dict_jogador = {
        'id': jogador[0],
        'nome': jogador[1],
        'idade': jogador[2],
        'posicao': jogador[3],
        'time': jogador[4]
    }
    desconectar_banco(conn, cursor)
    return dict_jogador

def editar_jogador_no_banco(id, nome, idade, posicao, time):
    conn = conectar_ou_criar_banco()
    cursor = criar_cursor(conn)
    criar_tabela_jogadores(cursor)
    cursor.execute('''
        UPDATE jogadores
        SET nome = ?, idade = ?, posicao = ?, time = ?
        WHERE id = ?''', (nome, idade, posicao, time, id))
    commitar_alteracoes(conn)
    desconectar_banco(conn, cursor)