from flask import (Flask, render_template, request, redirect, session)

app = Flask(__name__)
app.secret_key = 'RF81NbOd'

user = {"username": "abc", "password": "xyz"}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == user["username"] and password == user["password"]:
            session['username'] = username
            return redirect('/dashboard')

        return "<h1>Invalid login details</h1>"

@app.route('/dashboard')
def dashboard():
    if('user' in session and session['user'] == user['username']):
        return '<h1>Welcome to dashboard</h1>'

    return '<h1>Please login first</h1>'

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)