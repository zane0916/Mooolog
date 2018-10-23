import sqlite3

db = sqlite3.connect("Mooolog.db")
c = db.cursor()
command = ""

command = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, password TEXT)"
c.execute(command)

command = "CREATE TABLE IF NOT EXISTS blogs (blog_id INTEGER PRIMARY KEY, user_id INTEGER, title TEXT UNIQUE NOT NULL, category TEXT, author TEXT, time_stamp TEXT)"
c.execute(command)
