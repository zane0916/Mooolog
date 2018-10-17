# Team Mooo - Brian Lee, Emily Lee, Thomas Lee, Joshua Weiner
# SoftDev1 pd6
# P00 -- The Art of Storytelling
# 2018-10-17

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"

app.debug=True
app.run()
