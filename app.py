from flask import Flask, render_template, request, redirect, flash
# from flask_login import LoginManager, login_user
from werkzeug.security import check_password_hash
# from app import app, db, User, Patient, Doctor, Appointment, Prescription, Medicine, Bill
from datetime import datetime, date, timedelta
app = Flask(__name__)

import sqlite3
conn = sqlite3.connect("database.db")
cursor = conn.cursor()


# @app.route('/')
# def login():
#     return render_template('/login')
#     # return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
def logi():

    def get_user(username, password):
        cursor.execute(
            "SELECT * FROM user WHERE username=? AND password=?",
            (username, password)
        )
        return cursor.fetchone()

    if request.method == 'POST':
        usern = request.form.get('username')
        passwd = request.form.get('password')
        user = get_user(usern, passwd)  
        

        if user:
            role = user[3] 
            if role == 'admin':
                return render_template('addash.html')
            elif role == 'doctor':
                return render_template('drdash.html')
            elif role == 'patient':
                return render_template('register.html')
        
        return render_template('login.html', error="Invalid username or password")



    # if request.method == 'POST':
    #     usern = request.form.get('username')
    #     passwd = request.form.get('password')
    
    # def get_user(username, password):
    #     cursor.execute(
    #         "SELECT * FROM user WHERE username=? AND password=?",
    #         (username, password)
    #     )
    #     return cursor.fetchone()
    
    # user = get_user(usern)
    

    # # if user:
    # if user and check_password_hash(user['password'], passwd):
    #     if user['role'] == 'admin':
    #         return render_template('addash.html')
    #     elif user['role'] == 'doctor':
    #         return render_template('drdash.html')
    #     elif user['role'] == 'patient':
    #         return render_template('register.html')
        # flash('Invalid username or password.', 'error')

    # if user and check_password(passwd, user['password']):  # compare hashed pw
    #     if user['role'] == 'admin':
    #         return render_template('addash.html')
    #     elif user['role'] == 'doctor':
    #         return render_template('drdash.html')
    #     elif user['role'] == 'patient':
    #         return render_template('register.html')


    # def check_user(username, password):
    #     cursor.execute(
    #         "SELECT * FROM user WHERE username=? AND password=?",
    #         (username, password)
    #     )
    #     user = cursor.fetchone()
    #     conn.close()
    #     return user
    
    # if usern and user.check_password(passwd):
    #         # login_user(user)
    #         if user.role == 'admin':
    #             return render_template('addash.html')
    #         elif user.role == 'doctor':
    #             return render_template('drdash.html')
    #         elif user.role == 'patient':
    #             return render_template('register.html')
        #flash('Invalid username or password.', 'error')
    # return render_template('/login.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usern = request.form.get('username')
        email = request.form.get('email')
        passwd = request.form.get('password')
        nam = request.form.get('name')
        phoneno = request.form.get('phone')

        try:               
                cursor.execute(
                    "INSERT INTO user (username, email, password, role, name, phone) VALUES (?, ?, ?, ?, ?, ?)", 
                    (usern, email, passwd, 'patient', nam, phoneno)
                )
                conn.commit()
                conn.close()
                return redirect('login.html')
                
        except sqlite3.IntegrityError:   
            return "Error: That username is already taken. <body align=center><a href='/templates/register.html'><h4>Try Again<h4></a>"
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)