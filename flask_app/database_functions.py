import sqlite3

database_link = "./static/data/database.db"

# ---------- Account Information ----------
# Verify User
def verify_user(email, password):
    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    result = cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password,))
        
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

    cursor.execute('INSERT INTO users(username, email, password) VALUES (?, ?, ?)', (username, email, password,))

    connect.commit()
    connect.close()

# Verify Premium
def verify_premium(email):
    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    result = cursor.execute('SELECT is_premium FROM users WHERE email = ?', (email,))
        
    is_premium = False
    
    if result[0][0] == "True":
        is_premium = True

    connect.close()
    return is_premium
