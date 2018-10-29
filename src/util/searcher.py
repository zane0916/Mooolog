import sqlite3
    
def search_user(user):

    db = sqlite3.connect("data/Mooolog.db")
    c = db.cursor()

    userlist = list(c.execute("SELECT username FROM users"))
    for i in range (len(userlist)):
        userlist[i] = userlist[i][0]
    return user in userlist

    db.close()

def search_blog(blog):

    db = sqlite3.connect("data/Mooolog.db")
    c = db.cursor()
        
    bloglist = list(c.execute("SELECT title FROM blogs"))
    for i in range (len(bloglist)):
        bloglist[i] = bloglist[i][0]
    return blog in bloglist

    db.close()

def search_entry(entry):

    db = sqlite3.connect("data/Mooolog.db")
    c = db.cursor()

    entrylist = list(c.execute("SELECT title FROM entries"))
    for i in range (len(entrylist)):
        entrylist[i] = entrylist[i][0]
    return entry in entrylist
    
    db.close()
