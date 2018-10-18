import sqlite3

def register_user(username, password):
    db = sqlite3.connect("../data/Mooolog.db")
    c = db.cursor()
    command = "INSERT INTO users (username, password) VALUES(?, ?);"
    c.execute(command, (username, password))
    db.commit()
    db.close()

def login_user(username, password):
    db = sqlite3.connect("../data/Mooolog.db")
    c = db.cursor()
    command = "SELECT username, password FROM users;"
    c.execute(command)
    for user in c:
        if username == user[0] and password == user[1]:
            print("Success")
            db.close()
            return
    print("Error")
    db.close()
    return

# tests
# register_user("test", "test2")
# login_user("test", "test2")
# login_user("aa", "test2")
# login_user("test", "aa")
