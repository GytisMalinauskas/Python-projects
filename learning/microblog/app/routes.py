"""A view function module"""
from learning.microblog.app import app
from flask import render_template
from learning.microblog.app.forms import LoginForm
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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title='Sing In', form = form)