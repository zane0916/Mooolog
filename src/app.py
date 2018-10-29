# Team Mooo - Brian Lee, Emily Lee, Thomas Lee, Joshua Weiner
# SoftDev1 pd6
# P00 -- The Art of Storytelling
# 2018-10-17

from flask import Flask, session, render_template, url_for, redirect, request, flash
from datetime import datetime
from util import authenticate, make_blog, searcher, entry_control
import os

app = Flask(__name__)
app.secret_key=os.urandom(32)

@app.route('/')
def main():
    username = authenticate.is_loggedin(session)
    if username:
        return redirect(url_for('userpage', username=username))
    return render_template("main.html")

@app.route('/register', methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        return render_template("register.html")
    else:
        success, message = authenticate.register_user(
                request.form['username'],
                request.form['password'],
                request.form['re-enter password'])
        flash(message)
        if success:
            return render_template("/main.html")
        else:
            return redirect(url_for('reg'))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        username = authenticate.is_loggedin(session)
        if username:
            flash("You are already logged in!")
            return redirect(url_for('userpage', username=username))
        else:
            return render_template("login.html")
    else:
        success, message = authenticate.login_user(
                request.form['username'],
                request.form['password'])
        flash(message)
        if success:
            session['loggedin']=request.form['username']
            return redirect(url_for('userpage', username=request.form['username']))
        else:
            return redirect(url_for('login'))

@app.route('/user/<username>')
def userpage(username):
    if authenticate.user_exists(username):
        user_id = make_blog.find_id(username)
        blogs = make_blog.get_titles(user_id)
        # print(blogs)
        return render_template("userpage.html",
                username=username,
                blogs=blogs,
                loggedin=authenticate.is_loggedin(session))
    else:
        flash("User does not exist")
        return redirect(url_for('main'))

@app.route('/logout', methods=["GET", "POST"])
def logout():
    if authenticate.is_loggedin(session):
        session.pop('loggedin')
        flash("Successfully logged out.")
    else:
        flash("You are not logged in.")
    return redirect(url_for('main'))

@app.route('/create', methods=["GET", "POST"])
def create():
    if not authenticate.is_loggedin(session):
        flash("You must be logged in to create a blog")
        return redirect(url_for('main'))
    elif request.method=="GET":
        return render_template("create.html")
    else:
        time = str(datetime.now())
        # print(request.form['title'])
        success, message = make_blog.create(
            request.form['title'],
            request.form['category'],
            session['loggedin'],
            time
        )
        flash(message)
        if success:
            return redirect(url_for('userpage', username=session['loggedin']))
        else:
            return redirect(url_for('create'))

@app.route('/blog/<title>', methods=["GET", "POST"])
def blog(title):
    if not authenticate.is_loggedin(session):
        flash("You must be logged in to view blogs")
        return redirect(url_for('main'))
    if request.method=="GET":
        if make_blog.blog_exists(title):
            user_id = authenticate.get_userid(session)
            # print(user_id)
            name = title
            blog=make_blog.get_blog(title)
            # print(blog[1])
            entries=make_blog.get_entries(blog[0])
            # print(entries)
            return render_template("blog.html",name=name,blog=blog, entries=entries, user_id=user_id)
        else:
            flash("Blog does not exist")
            return redirect(url_for('main'))
    else:
        time = str(datetime.now())
        blog=make_blog.get_blog(title)
        blog_id = blog[0]
        success, message = entry_control.create_entry(
                blog_id,
                request.form['title'],
                request.form['content'],
                time
        )
        flash(message)
        return redirect(url_for('blog', title=title))

@app.route('/delete_entry/<entry_id>', methods=["GET"])
def delete_entry(entry_id):
    username = authenticate.is_loggedin(session)
    if not username:
        flash("You must be logged in to delete entries.")
        return redirect(url_for("main"))
    entry = entry_control.get_entry(entry_id)
    if not entry:
        flash("Entry does not exist.")
        return redirect(url_for("main"))
    blog_id = entry[1]
    blog = make_blog.get_blog_from_id(blog_id)
    if username != blog[4]:
        flash("You may only delete your own entries.")
        return redirect(url_for("blog", title=blog[2]))
    entry_control.delete_entry(entry_id)
    flash("Successfully deleted entry.")
    return redirect(url_for("blog", title=blog[2]))

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/searchResults')
def result():
    item = request.args['item']
    return render_template('searchresults.html',
                           item = item,
                           userin = searcher.search_user(item),
                           blogin = searcher.search_blog(item),
                           loggedin=authenticate.is_loggedin(session)
                           )

    '''
    success, message = searcher.search(item)
    if success:
        return redirect(url_for('userpage', username = item))
    else:
        flash(message)
        return redirect(url_for('search'))
    '''
    
if __name__ == "__main__":
    app.debug=True
    app.run()
