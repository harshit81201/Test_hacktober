# Import flask

from flask import Flask

# make flask app instance

app = Flask(__name__)

# route to home page

@app.route('/')

def home():
    return "<h1>Jai PUBG!</h1>"