import sqlite3

db = sqlite3.connect("data/Mooolog.db")
c = db.cursor()
command = ""

command = "DROP TABLE users"
c.execute(command)
command = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, password TEXT);"
c.execute(command)

command = "DROP TABLE blogs"
c.execute(command)
command = "CREATE TABLE IF NOT EXISTS blogs (blog_id INTEGER PRIMARY KEY, user_id INTEGER, title TEXT UNIQUE NOT NULL, category TEXT, author TEXT, timestamp TEXT);"
c.execute(command)
