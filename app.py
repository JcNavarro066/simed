from flask import Flask, render_template, request
from flask_db2 import DB2

app = Flask(__name__)

app.config['DB2_DATABASE'] = 'BLUDB'
app.config['DB2_HOSTNAME'] = 'dashdb-txn-sbox-yp-dal09-08.services.dal.bluemix.net'
app.config['DB2_PORT'] = 50000
app.config['DB2_PROTOCOL'] = 'TCPIP'
app.config['DB2_USER'] = 'vnx75949'
app.config['DB2_PASSWORD'] = '14ww1r21s31q8l@b'

db = DB2(app)


@app.route('/')
def hello():
    return 'Hello'


@app.route('/user', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        F_Name = request.form['F_Name']
        L_Name = request.form['L_Name']
        #cur = db.connection.cursor()
        #cur.execute('INSERT INTO tblUser (F_Name \, L_Name) VALUES (%s, %s, %s)', (F_Name, L_Name))
        #response = cur.fetchall()
        print(F_Name)
        print(L_Name)

    return render_template('user.html')


@app.route('/users')
def users():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM tblUser')
    response = cur.fetchall()
    print(response)
