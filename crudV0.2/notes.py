import sqlite3

def connect_db():
    conn = sqlite3.connect("notes.db")
    return conn

def drop_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS notes")  # Удаляем старую таблицу
    conn.commit()
    conn.close()

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

def create_note(title, content):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()  # ← добавил commit(), чтобы изменения сохранялись
    conn.close()

def read_notes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    conn.close()
    return notes

def update_note(note_id, title, content):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (title, content, note_id))
    conn.commit()
    conn.close()

def delete_note(note_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))  # ← Запятая нужна, чтобы передавать tuple
    conn.commit()
    conn.close()