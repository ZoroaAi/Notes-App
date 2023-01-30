#  Initialise Flask
from flask import Flask

def create_app():
    app = Flask(__name__) 
    # encrypt session data and cookies
    app.config['SECRET_KEY'] = 'BUBBLEGUM123'
    return app
