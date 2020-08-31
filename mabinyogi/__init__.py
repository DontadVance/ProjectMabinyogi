from flask import Flask

#creating the Flask app!
app = Flask(__name__)

#setting the secret key, used for debugging the flask website
app.config['SECRET_KEY'] = 'debug_passw0rd'

#importing the routes into the __init__ file so that it is imported to the run.py file (will explain, just ask)
from mabinyogi import routes
