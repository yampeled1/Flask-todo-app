from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/yampe/PycharmProjects/todo-app/todo.db'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    done = db.Column(db.Boolean)

@app.route('/')
def index():
    incomplete = Todo.query.filter_by(done=False).all()
    complete = Todo.query.filter_by(done=True).all()

    return  render_template('index.html' , incomplete=incomplete, complete=complete)

@app.route('/add', methods=['POST'])
def add():
    todo = Todo(text=request.form['todoItem'], done=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/done/<id>')
def done(id):

    todo = Todo.query.filter_by(id=int(id)).first()
    todo.done = True
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)