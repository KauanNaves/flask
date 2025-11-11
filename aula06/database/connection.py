import sqlite3
import os


def create_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'notes.db')
    conn = sqlite3.connect(db_path)
    return conn


def create_cursor(conn):
    cursor = conn.cursor()
    return cursor


def commit_connection(conn):
    conn.commit()


def create_table_notes():
    conn = create_connection()
    cursor = create_cursor(conn)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   note1 REAL NOT NULL,
                   note2 REAL NOT NULL,
                   note3 REAL NOT NULL,
                   average REAL NOT NULL);
""")
    commit_connection(conn)
    close_connection(conn, cursor)


def insert_student(name, note1, note2, note3, average):
    conn = create_connection()
    cursor = create_cursor(conn)
    cursor.execute("""
         INSERT INTO notes (name, note1, note2, note3, average) 
                VALUES (?, ?, ?, ?, ?);""",
                (name, note1, note2, note3, average))
    commit_connection(conn)
    close_connection(conn, cursor)


def get_all_notes():
    conn = create_connection()
    cursor = create_cursor(conn)
    cursor.execute("""
                   SELECT * FROM notes;""")
    results = cursor.fetchall()
    results_list = []
    for note in results:
        result_dict = {
            'id': note[0],
            'name': note[1],
            'note1': note[2],
            'note2': note[3],
            'note3': note[4],
            'average': note[5],
        } 
        results_list.append(result_dict)
    close_connection(conn, cursor)
    return results_list


def get_note_by_id(note_id):
    conn = create_connection()
    cursor = create_cursor(conn)
    cursor.execute("""
                   SELECT * FROM notes
                   WHERE id = ?;""", (note_id,))
    note = cursor.fetchone()
    result_dict = {
        'id': note[0],
        'name': note[1],
        'note1': note[2],
        'note2': note[3],
        'note3': note[4],
        'average': note[5],
    }
    close_connection(conn, cursor)
    return result_dict


def edit_note(note_id, name, note1, note2, note3, average):
    conn = create_connection()
    cursor = create_cursor(conn)
    cursor.execute("""
                   UPDATE notes
                   SET name = ?, note1 = ?, note2 = ?, note3 = ?, average = ?
                   WHERE id = ?;""",
                   (name, note1, note2, note3, average, note_id,))
    commit_connection(conn)
    close_connection(conn, cursor)


def delete_note(note_id):
    conn = create_connection()
    cursor = create_cursor(conn)
    cursor.execute("""
                   DELETE FROM notes
                   WHERE id = ?;""",
                   (note_id,))
    commit_connection(conn)
    close_connection(conn, cursor)


def calculate_average(note1, note2, note3):
    average = (float(note1) + float(note2) + float(note3)) / 3
    average = round(average, 2)
    return average


def close_connection(conn, cursor):
    cursor.close()
    conn.close()