"""To make /app a package"""
# when importing a package, __init__.py executes
# and defines what symbols the package exposes to the outside
from flask import Flask
from learning.microblog.config import Config
# __name__ of the module which it use, in this case /app
# app is a member of /app package
app = Flask(__name__)
app.config.from_object(Config)
# avoid circular imports
from learning.microblog.app import routes