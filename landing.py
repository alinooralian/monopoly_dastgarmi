import re
import uuid

def signup():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    email = input("Enter your email: ")
    
    for i in users:
        if users[i][0] == username:
            print("This username is already registered.")
            return False
    
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if not re.match(pattern, email):
        print("This email is invalid.")
        return False
    
    if len(password) < 8:
        print("Password length must be at least 8 characters.")
        return False
    
    userid = str(uuid.uuid4())
    users[userid] = [username, password, email]
    players[userid] = {
        "username" : username,
    }
    
    return True
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    check = False
    for i in users:
        if users[i][0] == username:
            check = True
            if users[i][1] == password:
                players[i] = {
                    "username" : username,
                }
                return True
            break
    
    if check:
        print("The password is invalid.")
    else:
        print("Username not found.")
    
    return False

users = {
    "user_id" : ["username", "password", "email"],
}
players = {
    "user_id" : ["username", "password", "email"],
}

print("1.New Game")
print("2.Load Game")
print("3.Leaderboard")
print("4.Exit")
key = input()

if key == '1':
    cnt = 0
    while cnt < 4:
        print("1.Singup")
        print("2.Login")
        print("3.Exit")
        key = input()
        
        if key == '1':
            while True:
                if signup():
                    break
        
        if key == '2':
            while True:
                if login():
                    break
        
        if key == '3':
            exit()
        
        cnt += 1