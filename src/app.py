# Team Mooo - Brian Lee, Emily Lee, Thomas Lee, Joshua Weiner
# SoftDev1 pd6
# P00 -- The Art of Storytelling
# 2018-10-17

from flask import Flask, session, render_template, url_for, redirect, request, flash
from datetime import datetime
from util import authenticate, make_blog
import os
import sqlite3

app = Flask(__name__)
app.secret_key=os.urandom(32)

@app.route('/')
def main():
    if session.get('loggedin') is None:
        return render_template("main.html")
    else:
        return redirect(url_for('userpage', username=session['loggedin']))

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
            return redirect(url_for('userpage', username=request.form['username']))
        else:
            return redirect(url_for('login'))

@app.route('/user/<username>')
def userpage(username):
    if authenticate.user_exists(username):
        with sqlite3.connect("data/Mooolog.db") as db:
            c = db.cursor()
            command = "SELECT user_id FROM users WHERE username = ?"
            c.execute(command, (username,))
            user_id = c.fetchone()[0]
            command = "SELECT title FROM blogs WHERE user_id = ?"
            blogs = c.execute(command, (user_id,))
        return render_template("userpage.html", username=username, blogs=blogs)
    else:
        return "temp"

@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.pop('loggedin')
    return redirect(url_for('login'))

@app.route('/create', methods=["GET", "POST"])
def create():
    if session.get('loggedin') is None:
        flash("You must be logged in to create a post")
        return redirect(url_for('main'))
    elif request.method=="GET":
        return render_template("create.html")
    else:
        time = str(datetime.now())
        print(request.form['title'])
        success, message = make_blog.create(
            request.form['title'],
            request.form['category'],
            session['loggedin'],
            time
        )
        flash(message)
        if success:
            return redirect(url_for('userpage', username=session['loggedin']))
        else:
            return redirect(url_for('create'))


if __name__ == "__main__":
    app.debug=True
    app.run()
