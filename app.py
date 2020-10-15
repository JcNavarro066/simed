from flask import Flask, render_template
from flask_db2 import DB2

app = Flask(__name__)

app.config['DB2_DATABASE'] = 'BLUDB'
app.config['DB2_HOSTNAME'] = 'dashdb-txn-sbox-yp-dal09-08.services.dal.bluemix.net'
app.config['DB2_PORT'] = 50000
app.config['DB2_PROTOCOL'] = 'TCPIP'
app.config['DB2_USER'] = 'vnx75949'
app.config['DB2_PASSWORD'] = '14ww1r21s31q8l@b'

db = DB2(app)


@app.route('/home')
def hello():
    return 'Hello'


@app.route('/')
def login():
    return render_template('index.html')


@app.route('/users')
def users():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM tblUser')
    response = cur.fetchall()
    print(response)
