from flask import Flask,render_template,url_for,request,redirect,jsonify
import mysql.connector

app=Flask(__name__)

conn=mysql.connector.connect(host="sql7.freesqldatabase.com",user="sql7630864",password="2gSVQDaWN7",database="sql7630864")
cursor=conn.cursor()
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/painting')
def painting():
    return render_template('painting.html')
@app.route('/login_validation',methods=["POST"])
def login_validation():
    email=request.form.get("email")
    password=request.form.get("Password")
    cursor.execute(""" SELECT * FROM `user` WHERE `email` LIKE '{}' and `password` LIKE '{}' """.format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
        return render_template('painting.html')
    else:
        return render_template('login.html')
@app.route('/register_validation',methods=["POST"])
def register_validation():
    name=request.form.get("name")
    email=request.form.get("email")
    password=request.form.get("Password")
    cursor.execute(""" INSERT INTO `users` (`name`,`email`,`password`) VALUES ('{}','{}','{}')""".format(name,email,password))
    conn.commit()
    return "User registered sucessfully"

if __name__=='__main__':
    app.run(debug=True)



