"""Main application module"""
# Flask needs to be told how to import it by setting the
# FLASK_APP env variable with "set" or "export" or use .env file:
# ! set FLASK_APP=microblog.py
# after setting env, run the app with:
# ! flask run or python.exe microblog.py
# you may now open http://127.0.0.1:5000
from app import app
from livereload import Server

def main():
    # Initializes Web Server Gateway Interface (WSGI) app
    # with live reload
    server = Server(app.wsgi_app)
    # watches templates and static files
    server.watch('app/templates/')
    server.watch('app/static/')
    # while in debug mode and on port 5000
    server.serve(port=5000, debug=True)
    
if __name__ == "__main__":
    main()