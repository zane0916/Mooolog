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
        command="INSERT INTO blogs (user_id, title, category, author, timestamp) VALUES(?, ?, ?, ?, ?);"
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

def find_id(u_name):
    with sqlite3.connect("data/Mooolog.db") as db:
        c = db.cursor()
        command = "SELECT user_id FROM users WHERE username=?"
        c.execute(command, (u_name,))
        id = c.fetchall()
        return id[0][0]

def get_titles(u_id):
    with sqlite3.connect("data/Mooolog.db") as db:
        c = db.cursor()
        command = "SELECT * FROM blogs WHERE user_id=?"
        c.execute(command, (u_id,))
        blogs = c.fetchall()
        return blogs

def get_blog(u_title):
    with sqlite3.connect("data/Mooolog.db") as db:
        c = db.cursor()
        command = "SELECT * FROM blogs WHERE title=?"
        c.execute(command, (u_title,))
        blogs = c.fetchall()
        return blogs[0]

def get_entries(b_id):
    with sqlite3.connect("data/Mooolog.db") as db:
        c = db.cursor()
        command = "SELECT * FROM entries WHERE blog_id=?"
        c.execute(command, (b_id,))
        return c.fetchall()
