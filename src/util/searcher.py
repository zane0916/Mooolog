import sqlite3

def search(user):

    db = sqlite3.connect("data/Mooolog.db")
    c = db.cursor()

    userlist = list(c.execute("SELECT username FROM users"))
    for i in range (len(userlist)):
        userlist[i] = userlist[i][0]
    if user in userlist:
        return (True, '')
    else:
        return (False, "User {} does not exist. Please try again.".format(user))

    db.close()
