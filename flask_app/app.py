from flask import Flask, render_template, request, redirect, url_for
import requests
import database_functions as dbf

# ---------- Login/Signup ----------
# Login
@app.route("/login")
def login():
    return render_template("login.html")

# Sign Up
@app.route("/signup")
def signup():
    return render_template("signup.html")

# Verify User
@app.route("/verify-user", methods=['GET', 'POST'])
def verify_user():
    global current_user
    global current_email

    username = ""
    email = request.form['email']
    password = request.form['password']

    current_user = dbf.verify_user(email, password)

    if current_user != "":
        current_email = email

        return redirect(url_for('home'))
    else:
        return render_template('login.html', message='Invalid Gmail or Password, Please Try Again')

# Store User
@app.route('/store-user', methods=['GET', 'POST'])
def store_user():
    global current_user
    global current_email

    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    if dbf.get_user_rowid(email) == "":
        dbf.signup_user(username, email, password)

        current_user = username
        current_email = email

        return redirect(url_for('home'))

    else:
        return render_template('login.html', message="Email Already In Use, Log In Instead?")

# Log Out
@app.route('/logout')
def logout():
    global current_user
    global current_email

    current_user = ""
    current_email = ""

    return render_template('home.html', current_user=current_user, logout_message='Successfully Logged Out!')