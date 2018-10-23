# Mooolog

How to run our project:

If flask is not installed:<br>
1. Download python3<br>
2. To create a virtual environment:<br>
	- python3 -m venv <venv><br>
3. Activate the virtual environment:<br>
	- . <venv>/bin/activate<br>
4. While in the virtual environment:<br>
	- pip3 install wheel<br>
	- pip3 install flask

To run the code:
	python src/app.py
- Home page should show up with options to register or to login.
- Register redirects you to a page to create a username and passwords-
  the username must not already exist and the passwords must match.
- Login sends you to a page to enter your username and password,
  which must both exist and match.
	- Successful logins send you to a welcome page where you can
	  create blogs.
