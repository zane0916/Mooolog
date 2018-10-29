import sqlite3

def create_entry(blog_id, title, content, timestamp):
    db = sqlite3.connect("data/Mooolog.db")
    c = db.cursor()
    if title=="" or content=="" or timestamp is None:
        return(False, "Make sure all required fields are filled in")
    else:
        command="INSERT INTO entries (blog_id, title, content, timestamp) VALUES(?, ?, ?, ?);"
        c.execute(command, (blog_id, title, content, timestamp))
    db.commit()
    return (True, "Successfully created entry {}".format(title))

def delete_entry(entry_id):
    db = sqlite3.connect("data/Mooolog.db")
    c = db.cursor()
    command = "DELETE FROM entries WHERE entry_id = ?;"
    c.execute(command, (entry_id,))
    db.commit()
    return (True, "Succesfully deleted entry.")

def edit_entry(entry_id, title, content, timestamp):
    db = sqlite3.connect("data/Mooolog.db")
    c = db.cursor()
    if title=="" or content=="" or timestamp is None:
        return(False, "Make sure all required fields are filled in")
    else:
        command="UPDATE entries SET title = (?), content = (?), timestamp=(?) WHERE entry_id=(?);"
        c.execute(command, (title, content, timestamp, entry_id,))
    db.commit()
    return (True, "Successfully edited entry {}".format(title))

def get_entry(entry_id):
    '''
    Returns a list containing data about an entry given its ID.
    Returns None if the entry does not exist.
    '''
    db = sqlite3.connect("data/Mooolog.db")
    c = db.cursor()
    command = "SELECT * FROM entries WHERE entry_id = ?;"
    c.execute(command, (entry_id,))
    return c.fetchone()
