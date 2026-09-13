"""A view function module"""
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
# Decorator modifies function that follows it
# Callback for certain event
# In this case:
# creates an association between URL as argument and function.
# Meaning when browser requests these URLs,
# the function "index" is going to be invoked
# and pass its return value as a response
@app.route("/")
@app.route("/index")
def index():
    user = {"name": "Gytis", "username": "Fare"}
    posts = [
        {
            "author": {"username": "Atene"},
            "body": "Good day, sir" 
        },
        {
            "author": {"username": "Patrik"},
            "body": "Good day, mrs Atene"
        }
    ]
    return render_template("index.html", title = user["username"], name = user["name"], posts=posts)

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html", title='Sing In', form = form)