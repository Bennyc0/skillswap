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

    cursor.execute('INSERT INTO users(username, email, password, is_premium) VALUES (?, ?, ?)', (username, email, password, "false",))

    connect.commit()
    connect.close()

# Verify Premium
def verify_premium(email):
    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    result = cursor.execute('SELECT is_premium FROM users WHERE email = ?', (email,))
        
    is_premium = False
    
    if (item[0] for item in result) == "true":
        is_premium = True

    connect.close()
    return is_premium


# ---------- Posts ----------
def store_posts(post_info):
    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    cursor.execute('INSERT INTO ss_posts(poster_email, poster_name, category, title, description, contact_info) VALUES (?, ?, ?, ?, ?, ?)', (post_info[0], post_info[1], post_info[2], post_info[3], post_info[4], post_info[5],))

    connect.commit()
    connect.close()


def get_posts(category):
    connect = sqlite3.connect(database_link)
    cursor = connect.cursor()

    if category:
        result = cursor.execute('SELECT * FROM ss_posts WHERE category = ?', (category,))
    else:
        result = cursor.execute('SELECT * FROM ss_posts')

    all_posts = []
    information = {
        "something": None,
    }
    
    for item in result:
        information = {
            "poster_email": item[0],
            "poster_name": item[1],
            "category": item[2],
            "title": item[3],
            "description": item[4],
            "contact_info": item[5]
        }

        all_posts.append(information)
    
    return all_posts


# ---------- AI Matching ----------
# (Not really AI matching)

# Free Version
# def ai_matching(skill):

# ---------- Profile ----------
def get_user_information(current_email):
    return None
