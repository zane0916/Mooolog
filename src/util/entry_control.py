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
