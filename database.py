import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(
                'CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, name TEXT NOT NULL)'
            )

    def add_task(self, task_name):
        with self.connection:
            self.connection.execute('INSERT INTO tasks (name) VALUES (?)', (task_name,))

    def get_tasks(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM tasks')
        return cursor.fetchall()
    
    def remove_task(self, task_id):
        with self.connection:
            self.connection.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
