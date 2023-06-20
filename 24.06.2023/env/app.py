from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)


db_connection = psycopg2.connect(
    host='localhost',
    database='book',
    user='alema',
    password='iglikovtishka2006'
)

@app.route('/')
def index():

    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY id")
    tasks = cursor.fetchall()
    cursor.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():

    title = request.form['title']
    description = request.form['description']
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO tasks (title, description) VALUES (%s, %s)", (title, description))
    db_connection.commit()
    cursor.close()
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):

    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    db_connection.commit()
    cursor.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
