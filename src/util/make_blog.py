import sqlite3


def create(title, category, username, timestamp):
    db = sqlite3.connect("data/Mooolog.db")
    c = db.cursor()
    if title=="" or category=="" or username=="" or timestamp is None:
        return(False, "Make sure all required fields are filled in")

    if blog_exists(title):
        return(False, "A blog with title {} already exists".format(title))
    else:
        user_num = find_id(username)
        command="INSERT INTO blogs (user_id, title, category, author, time_stamp) VALUES(?, ?, ?, ?, ?);"
        c.execute(command, (user_num, title, category, username, timestamp))

    db.commit()
    return (True, "Successfully created blog {}".format(title))

def blog_exists(title):
    '''
    Returns whether a blog with the given title exists
    '''
    with sqlite3.connect("data/Mooolog.db") as db:
        c = db.cursor()
        command = "SELECT * FROM blogs WHERE title = ?"
        c.execute(command, (title,))

        return len(c.fetchall()) > 0

def find_id(username):
    with sqlite3.connect("data/Mooolog.db") as db:
        c = db.cursor()
        command = "SELECT user_id FROM users WHERE username = ?"
        id = c.execute(command, (username,))
        return id
