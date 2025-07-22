import os
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

DB_PATH = os.path.join('data', 'blog.db')

# Initialize the database only if it doesn't exist
def init_db():
    if not os.path.exists(DB_PATH):
        os.makedirs('data', exist_ok=True)
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

init_db()  # only runs if DB doesn't exist


@app.route('/')
def index():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM posts ORDER BY timestamp DESC")
    posts = c.fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO posts (title, content, timestamp) VALUES (?, ?, ?)",
                  (title, content, timestamp))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('new.html')


@app.route('/post/<int:post_id>')
def show_post(post_id):
    conn = sqlite3.connect(DB_PATH)  # ✅ Use the shared DB_PATH
    c = conn.cursor()
    c.execute("SELECT * FROM posts WHERE id=?", (post_id,))
    post = c.fetchone()
    conn.close()
    return render_template('post.html', post=post)


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=True)
