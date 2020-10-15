from flask import Flask, render_template, request, redirect, url_for, flash
from flask_db2 import DB2
# from database import database

app = Flask(__name__)

app.config['DB2_DATABASE'] = 'BLUDB'
app.config['DB2_HOSTNAME'] = 'dashdb-txn-sbox-yp-dal09-08.services.dal.bluemix.net'
app.config['DB2_PORT'] = 50000
app.config['DB2_PROTOCOL'] = 'TCPIP'
app.config['DB2_USER'] = 'vnx75949'
app.config['DB2_PASSWORD'] = '14ww1r21s31q8l@b'

db = DB2(app)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        age = request.form['age']
        dateBirth = request.form['datebirth']
        gender = request.form['gender']
        email = request.form['email']
        password = request.form['password']
        isDoctor = request.form.__contains__('isDoctor')
        cur = db.connection.cursor()
        query = '''INSERT INTO tblUser (email , password, f_name, l_name, dateOfBirth, age, gender)
                    VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')''' % (email, password, name, lastname, dateBirth, age, gender)
        cur.execute(query)
        if (isDoctor):
            return redirect(url_for('register_doctor'))
        return redirect(url_for('register_patient'))
    return render_template('auth/register.html')


@app.route('/register/doctor', methods=['POST', 'GET'])
def register_doctor():
    if request.method == 'POST':
        professionalRegister = request.form['professionalRegister']
        especialism = request.form['especialism']
        cur = db.connection.cursor()
        query = '''INSERT INTO tblDoctor (professionalRegister , especialism)
                    VALUES ('%s', '%s')''' % (professionalRegister, especialism)
        cur.execute(query)
        return redirect(url_for('login'))
    return render_template('auth/register_doctor.html')


@app.route('/register/patient', methods=['POST', 'GET'])
def register_patient():
    if request.method == 'POST':
        civilState = request.form['civilState']
        ocupation = request.form['ocupation']
        address = request.form['address']
        cur = db.connection.cursor()
        query = '''INSERT INTO tblPatient (civilState , ocupation, address)
                    VALUES ('%s', '%s', '%s')''' % (civilState, ocupation, address)
        cur.execute(query)
        return redirect(url_for('login'))
    return render_template('auth/register_patient.html')


@app.route('/')
def home(name=None):
    return render_template('home.html', user=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']

        cur = db.connection.cursor()
        query = '''SELECT f_name FROM tblUser WHERE email = '%s' AND password= '%s'
        ''' % (user, password)

        cur.execute(query)
        response = cur.fetchone()

        if (response is not None):
            query = '''INSERT INTO tbllogin (email , password)
                        VALUES ('%s', '%s')''' % (user, password)
            cur.execute(query)
            return redirect(url_for('home', name=response[0]))
        else:
            return redirect(url_for('register'))
    return render_template('auth/login.html')
