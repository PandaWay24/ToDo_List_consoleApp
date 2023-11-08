# Methods to create users and validate user logins
import main
import hashlib
import json
import os


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def new_user():
    print("--New User Sign Up--")

    # repeat asking for a new username if the username entered already exists
    while True:
        username = input("Enter New Username: ")

        # an option to cancel signup process and return to welcome screen
        if username == 'q':
            return False
        elif valid_user(username):
            break
        else:
            print("username already exists!! please try a different username or enter 'q' to return to welcome screen")
            continue

    while True:
        password = hash_password(input("Enter New Password: "))

        if password == hash_password(input("Re-Enter Password: ")):
            break
        else:
            print("Re-Entered password doesn't match the new password!! Recreate new password..")
            continue

    user = {"username": username, "password": password}

    if os.path.getsize("userData.json") != 0:
        with open("userData.json", 'r') as userData:
            users = json.load(userData)
            users.append(user)

        with open("userData.json", 'w') as userData:
            json.dump(users, userData, indent=4)
    else:
        with open("userData.json", 'w') as userData:
            json.dump([user], userData, indent=4)

    print("Account Successfully created!")
    return True


def login():
    pass


def valid_user(username):
    if os.path.getsize("userData.json") == 0:
        return True
    else:
        with open("userData.json", 'r') as userData:
            users = json.load(userData)
            for user in users:
                if username == user["username"]:
                    return False
                else:
                    continue
            return True


