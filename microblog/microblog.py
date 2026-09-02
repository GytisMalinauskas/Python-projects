"""Main application module"""
# Flask needs to be told how to import it by setting the
# FLASK_APP env variable with "set" or "export" or use .env file:
# ! set FLASK_APP=microblog.py
# after setting env, run the app with:
# ! flask run
# you may now open http://127.0.0.1:5000
from app import app