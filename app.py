from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import mysql.connector as conn

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Shoyeb@12'
app.config['MYSQL_DB'] = 'userdata'
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def registration_form():
    return render_template('registration_form.html')

@app.route('/register', methods=['POST'])

def register():
    if request.method == 'POST':
        # Fetch form data
        studname = request.form['studname']
        fathername = request.form['fathername']
        mothername = request.form['mothername']
        phnumber = request.form['phnumber']
        mail = request.form['mail']
        dob = request.form['dob']
        address = request.form['address']
        bloodgrp = request.form['bloodgrp']
        deptAdd = request.form['deptAdd']
        courseAdd = request.form['courseAdd']

        # Save data to MySQL
        mydb = conn.connect(host = "localhost", user = "root", passwd = "Shoyeb@12")
        cur = mydb.cursor()
        cur.execute("use userdata")
        cur.execute("INSERT INTO userinfo (studname, fathername, mothername, phnumber, mail, dob, address, bloodgrp, deptAdd, courseAdd) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (studname, fathername, mothername, phnumber, mail, dob, address, bloodgrp, deptAdd, courseAdd))
        mydb.commit()
        cur.close()

        # Redirect to the root endpoint
        return redirect('/')
    else:
        return "Method Not Allowed", 405
    

if __name__ == '__main__':
    app.run(debug=True)    