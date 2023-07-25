import sqlite3

database_link = "./static/data/database.db"

# ---------- Login/Signup ----------
# Verify User
def verify_user(email, password):
    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    result = cursor.execute('SELECT * FROM userbase WHERE email = ? AND password = ?', (email, password,))
        
    information = {
        "username": ""
    }
    
    for item in result:
        information = {
            "username": item[0]
        }

    connect.close()
    return information['username']

# Sign Up
def signup_user(username, email, password):
    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    cursor.execute('INSERT INTO userbase(username, email, password) VALUES (?, ?, ?)', (username, email, password,))

    connect.commit()
    connect.close()