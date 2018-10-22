# Team Mooo - Brian Lee, Emily Lee, Thomas Lee, Joshua Weiner
# SoftDev1 pd6
# P00 -- The Art of Storytelling
# 2018-10-17

from flask import Flask, session, render_template, url_for, redirect, request, flash
from util import authenticate
import os

app = Flask(__name__)
app.secret_key=os.urandom(32)

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/register', methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        return render_template("register.html")
    else:
        success, message = authenticate.register_user(
                request.form['username'], 
                request.form['password'],
                request.form['re-enter password'])
        flash(message)
        if success:
            return render_template("/main.html")
        else:
            return redirect(url_for('reg'))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        success, message = authenticate.login_user(
                request.form['username'],
                request.form['password'])
        flash(message)
        if success:
            session['loggedin']=request.form['username']
            # TODO: Probably should redirect to somewhere else
            return redirect(url_for('logged'));
        else:
            return redirect(url_for('login'))

@app.route('/welcome', methods=["GET", "POST"])
def logged():
    return render_template("logged.html", user=session['loggedin'])
    
@app.route('/logout', methods=["GET", "POST"])
def logout():
    print(session)
    session.pop('loggedin')
    print(session)
    return redirect(url_for('login'))

    
if __name__ == "__main__":
    app.debug=True
    app.run()
