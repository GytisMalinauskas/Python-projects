"""To make /app a package"""
# when importing a package, __init__.py executes
# and defines what symbols the package exposes to the outside
from flask import Flask

# __name__ of the module which it use, in this case /app
# app is a member of /app package
app = Flask(__name__)

# avoid circular imports
from app import routes