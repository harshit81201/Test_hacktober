from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample user data (in real applications, this data would be stored in a database)
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/xyz')
def xyz():
    return render_template('xyz.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Check if the username and password match the data in the 'users' dictionary
    if username in users and users[username] == password:
        return redirect('/xyz')
    else:
        return 'Invalid credentials. Please try again.'

if __name__ == '__main__':
    app.run(debug=True)
