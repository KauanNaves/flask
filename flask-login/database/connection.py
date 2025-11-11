import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'app.db')


def create_connection(db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_cursor(conn):
    if conn:
        return conn.cursor()
    return None


def commit_connection(conn):
    if conn:
        conn.commit()


def create_all_tables():
    create_table_users()
    create_table_properties()


def create_table_users():
    conn = create_connection()
    cursor = create_cursor(conn)
    if cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    date_created TEXT NOT NULL);
''')
        commit_connection(conn)
    close_connection(conn)


def add_user(name: str, email: str, password: str, date_created: str):
    conn = create_connection()
    cursor = create_cursor(conn)
    if cursor:
        cursor.execute('''
            INSERT INTO users (name, email, password, date_created)
            VALUES (?, ?, ?, ?)''', (name, email, password, date_created))
        commit_connection(conn)
    close_connection(conn)


def get_users_by_name(name: str):
    conn = create_connection()
    cursor = create_cursor(conn)
    result = []
    if cursor:
        cursor.execute('''
                       SELECT id FROM users
                       WHERE name = ?''', (name,))
        result = cursor.fetchone()
    close_connection(conn)
    return result


def email_exists(email: str) -> bool:
    conn = create_connection()
    cursor = create_cursor(conn)
    result = []
    if cursor:
        cursor.execute('SELECT id FROM users WHERE email = ?', (email,))
        result = cursor.fetchone()
    close_connection(conn)
    return result


def edit_user_password(email: str, new_password: str):
    conn = create_connection()
    cursor = create_cursor(conn)
    if cursor:
        cursor.execute('''
            UPDATE users
            SET password = ?
            WHERE email = ?''', (new_password, email))
        commit_connection(conn)
    close_connection(conn)


def edit_user_name(email: str, new_name: str):
    conn = create_connection()
    cursor = create_cursor(conn)
    if cursor:
        cursor.execute('''
                UPDATE users
                SET name = ?
                WHERE email = ?''', (new_name, email))
        commit_connection(conn)
    close_connection(conn)


def edit_user_email(old_email: str, new_email: str):
    conn = create_connection()
    cursor = create_cursor(conn)
    if cursor:
        cursor.execute('''
                UPDATE users
                SET email = ?
                WHERE email = ?''', (new_email, old_email))
        commit_connection(conn)
    close_connection(conn)


def delete_user(name: str) -> bool:
    conn = create_connection()
    cursor = create_cursor(conn)
    if cursor:
        result = get_users_by_name(name)
        if result:
            id_user = result
            cursor.execute('''
                        DELETE FROM users
                        WHERE id = ?''', (id_user,))
            commit_connection(conn)
    close_connection(conn)
    return True if result else False 


def create_table_properties():
    conn = create_connection()
    cursor = create_cursor(conn)
    if cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS properties (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    address TEXT NOT NULL,
                    price REAL NOT NULL,
                    type TEXT NOT NULL,
                    status TEXT NOT NULL,
                    date_created TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id));   
''')
        commit_connection(conn)
    close_connection(conn)


def close_connection(conn):
    if conn:
        conn.close()


