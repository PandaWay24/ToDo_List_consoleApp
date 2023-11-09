# Methods to create users and validate user logins
import hashlib
import json
import os
import time


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def new_user():
    os.system('cls')
    print("--New User Sign Up--\n")

    # repeat asking for a new username if the username entered already exists
    while True:
        username = input("Enter New Username: ")

        # an option to cancel signup process and return to welcome screen
        if username == 'q':
            return False, None
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
    return True, username


def login():
    os.system('cls')
    print("------Login to your account------\n")
    fail_count = 0
    while True:
        if fail_count < 5:
            username = input("Enter username: ")
            password = hash_password(input("Enter password:"))

            if os.path.getsize("userData.json") == 0:
                print("\nuser doesn't exist! create an account!\n")
                time.sleep(3)
                return False, None

            with open("userData.json", "r") as userJson:
                for user in json.load(userJson):
                    if username == user["username"]:
                        if password == user["password"]:
                            return True, username
                print("invalid username/password, please try again!")
                fail_count += 1
        else:
            print("Login failed too many times!!")
            return False, None


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


if __name__ == "__main__":
    login()
