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
def hello_world():
    return redirect(url_for('reg'))

@app.route('/register')
def reg():
    return render_template("/welcome.html")

@app.route('/auth', methods=["POST"])
def auth():
    print(request.form)
    return "x"

if __name__=="__main__":
    app.debug=True
    app.run()
