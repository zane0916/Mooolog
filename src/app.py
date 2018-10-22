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
            return redirect(url_for('userpage', username = request.form['username']));
        else:
            return redirect(url_for('login'))

@app.route('/user/<username>')
def userpage(username):
    if authenticate.user_exists(username):
        return render_template("userpage.html", username = username)
    else:
        return "temp"

if __name__ == "__main__":
    app.debug=True
    app.run()
