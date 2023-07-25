from flask import Flask, render_template, request, redirect, url_for
import requests
import database_functions as dbf

current_email = None
current_user = None

# ---------- Homepage ----------
# Home
@app.route("/")
def home():
    return render_template("home.html")


# ---------- Account Information ----------
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

    current_user = None
    current_email = None

    return render_template('home.html', current_user=current_user, logout_message='Successfully Logged Out!')


# ---------- Find ----------
@app.route('/find')
def find():


# ---------- Message ----------
@app.route('/message')
def message():
    return render_template('message.html')


# ---------- Profile ----------
@app.route('/profile')
def profile():
    global current_email

    information = dbf.get_user_information(current_email)

    return render_template('profile.html', information=information)

# ---------- About ----------
@app.route('/about')
def about():
    return render_template('about.html')

# ---------- Premium ----------
@app.route('/premium')
def premium():
    global current_email

    is_premium = dbf.verify_premium(current_email)

    return render_template('premium.html', is_premium=is_premium)

