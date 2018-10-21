import sqlite3

def register_user(username, password, repassword):
    '''
    Attempts to register a user and enter it in the users table.

    Returns a tuple containing a boolean indicating success,
    and an error message (empty if successful)
    '''
    if username == '' or password == '' or repassword == '':
        return (False, "Please fill in all fields.")
    elif password != repassword:
        return (False, "Passwords do not match!")

    db = sqlite3.connect("data/Mooolog.db")
    c = db.cursor()

    command = "INSERT INTO users (username, password) VALUES(?, ?);"
    c.execute(command, (username, password))

    db.commit()
    db.close()
    return (True, )

def login_user(username, password):
    db = sqlite3.connect("data/Mooolog.db")
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
