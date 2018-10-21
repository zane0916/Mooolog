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
    return render_template("/main.html")

@app.route('/register', methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        return render_template("/register.html")
    else:
        success, error = authenticate.register_user(
                request.form['username'], 
                request.form['password'],
                request.form['re-enter password'])
        if success:
            return render_template("/home.html",
                    user=request.form['username'])
        else:
            flash(error)
            return redirect(url_for('reg'))

if __name__ == "__main__":
    app.debug=True
    app.run()
