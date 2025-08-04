import sqlite3

class DB:

    def __init__(self,dbname='todo.db'):
        self.dbname = dbname
    def add_task(self,task_id,task=None,status = 'pending'):
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()
        # cursor.execute(
        #
        #     '''
        #     CREATE TABLE IF NOT EXISTS tasks(
        #     id INTEGER PRIMARY KEY AUTOINCREMENT,
        #     task TEXT NOT NULL,
        #     status TEXT NOT NULL DEFAULT 'pending'
        #     )
        #     '''
        # )

        cursor.execute('INSERT INTO tasks (id,task, status) VALUES (?, ? , ?)', (task_id,task, status))

        conn.commit()
        conn.close()
    def update_task(self,task_id,task=None,status=None):
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()
        if task and status:
            cursor.execute('UPDATE tasks SET task = ?,status = ? WHERE id=? ',(task,status,task_id))
        elif task:
            cursor.execute('UPDATE tasks SET task = ? WHERE id = ?', (task, task_id))
        elif status:
            cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (status, task_id))
        conn.commit()
        conn.close()

    def delete_task(self,task_id):
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()

    def display(self,task_id):
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        res = cursor.fetchone()
        conn.close()
        if res:
            print(f'Task ID:{res[0]},Task:{res[1]},status:{res[2]}')
        else:
            print(f'No task found with ID {task_id}')

if __name__ == '__main__':
    db = DB()

    db.add_task(1,'Finish homework','pending')

    db.update_task(1,task='Finish math homework', status='completed')

    db.display(1)

    # db.delete_task(1)
    print('Database initialized successful')



