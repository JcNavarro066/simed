from flask import Flask, render_template
#from flask_db2 import DB2

app= Flask(__name__)

#app.config['DB2_DATABASE'] =
#app.config['DB2_HOSTNAME'] =
#app.config['DB2_PORT'] =
#app.config['DB2_USER'] =
#app.config['DB2_PASSWORD'] =

#db = DB2

@app.route('/home')
def hello():
    return 'Hello'

@app.route('/')
def login():
    return render_template('index.html')

