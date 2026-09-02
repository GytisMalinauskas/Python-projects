"""A view function module"""
from app import app

# Decorator modifies function that follows it
# Callback for certain event
# In this case:
# creates an association between URL as argument and function.
# Meaning when browser requests these URLs,
# the function "index" is going to be invoked
# and pass its return value as a response
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"