import sqlite3

def register_user(username, password):
    db = sqlite3.connect("../data/Mooolog.db")
    c = db.cursor()
    command = "INSERT INTO users VALUES(?, ?)"
    c.execute(command, (username, password))

register_user("test", "test2")
