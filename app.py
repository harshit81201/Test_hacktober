from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')