from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'alema'
app.config['MYSQL_PASSWORD'] = 'iglikovtishka2006'
app.config['MYSQL_DB'] = 'todo_db'

mysql = MySQL(app)


class TodoTask:
    def __init__(self, id, title):
        self.id = id
        self.title = title


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks")
    result = cur.fetchall()
    tasks = [TodoTask(id=row[0], title=row[1]) for row in result]
    cur.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    mysql.connection.commit()
    cur.close()
    return redirect('/')

if __name__ == '__main__':
    app.run()
