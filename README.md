# Mooolog

How to run our project:

If flask is not installed:
1. Download python3
2. To create a virtual environment:
```
python3 -m venv <venv>
```
3. Activate the virtual environment:
```
. <venv>/bin/activate
```
4. While in the virtual environment:
```
pip3 install wheel
pip3 install flask
```

If running for the first time, the SQLite database must be initialized.
Go to the `src\data` directory and run:
```
python init_table.py
```
(It will also reset the database if one already exists.)

To run the code, go to the `src` directory and run:
```
python app.py
```

- Home page should show up with options to register or to login.
- Register redirects you to a page to create a username and passwords-
  the username must not already exist and the passwords must match.
- Login sends you to a page to enter your username and password,
  which must both exist and match.
	- Successful logins send you to a welcome page where you can
	  create blogs.

## Modules Used

### datetime
[Documentation](https://docs.python.org/3/library/datetime.html)

Provides access to time. 
It was used to record when each blog post was made.

### werkzeug
[Documentation](http://werkzeug.pocoo.org/)

Provided hashing functions since passwords should not be stored as plaintext for security.
Passwords are stored in the database as hashes created by werkzeug and checked by hashing the user's input and comparing it to the hashed password.
