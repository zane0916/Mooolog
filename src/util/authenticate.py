import sqlite3

def register_user(username, password, repassword):
    '''
    Attempts to register a user and enter it in the users table.

    Returns a tuple containing a boolean indicating success
    and a message to flash to the user.
    '''
    if username == '' or password == '' or repassword == '':
        return (False, "Please fill in all fields.")
    elif password != repassword:
        return (False, "Passwords do not match!")

    with sqlite3.connect("data/Mooolog.db") as db:
        c = db.cursor()

        # TODO: Check if username already exists
        command = "INSERT INTO users (username, password) VALUES(?, ?);"
        c.execute(command, (username, password))

        db.commit()
    return (True, "Successfully registered {}".format(username))

def login_user(username, password):
    '''
    Attempts to log in a user by checking the users table.

    Returns a tuple containing a boolean indicating success
    and a message to flash to the user.
    '''
    if username == '' or password == '':
        return (False, "Username or password missing!")

    with sqlite3.connect("data/Mooolog.db") as db:
        c = db.cursor()
        command = "SELECT username, password FROM users;"
        c.execute(command)
        for user in c:
            if user and username == user[0] and password == user[1]:
                return (True, "Successfully logged in!")
    return (False, "Incorrect username or password.")

# tests
# register_user("test", "test2")
# login_user("test", "test2")
# login_user("aa", "test2")
# login_user("test", "aa")
