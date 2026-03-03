from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Database Function
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('username')
    email = request.form.get('email')

    # Save to Database 
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

    return f"<h1>Successful!</h1><p>{name} is saved to database</p><br><a href='/view'>TO VIEW</a>"

# To View Route
@app.route('/view')
def view_users():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    return  render_template('view.html' ,users=rows)

if __name__ == '__main__' :
    init_db()
    # Build a DB right after an app
    app.run(debug=True,port=5000,use_reloader=False)
