# Methods to create users and validate user logins
import hashlib
import json
import os
import time


# To not store password in plain text, a small security measure
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


# Method for creating new user account
def new_user():
    # cleans the terminal and prints title of the current screen
    os.system('cls')
    print("--New User Sign Up--\n")
    print("You can enter 'q' to return to welcome screen!")
    # repeat asking for a new username if the username entered already exists
    while True:
        username = input("Enter New Username: ")

        # an option to cancel signup process and return to welcome screen
        if username == 'q':
            return False, None
        # any other input will be validated by checking its availability
        # if it is available, method will return true, and we break out of this loop
        elif valid_user(username):
            break
        # if the valid_user() didn't return true following error is printed and loop continues
        # giving user a chance to whether type new username or quit to the welcome screen and login
        else:
            print("username already exists!! please try a different username or enter 'q' to return to welcome screen")
            continue

    # password is asked to enter twice and compared one another
    # looping until both matches
    password_fails = 0
    while password_fails < 5:
        print("You can enter 'q' to return to welcome screen!")
        password = hash_password(input("Enter New Password: "))
        if password == hash_password('q'):
            return
        elif password == hash_password(input("Re-Enter Password: ")):
            break
        else:
            print("Re-Entered password doesn't match the new password!! Please try again!!..")
            password_fails += 1
            continue

    if password_fails >= 5:
        return
    # python dict to save the user in a json file
    user = {"username": username, "password": password}

    # this check if the user data file is currently not empty,
    # and append new user to the existing list of user
    if os.path.getsize("userData.json") != 0:
        with open("userData.json", 'r') as userData:
            # loads the json user data and append the 'user' dict to it. user dicts are stored in a list
            users = json.load(userData)
            users.append(user)

        # Then the new list is dumped back to the json file
        with open("userData.json", 'w') as userData:
            json.dump(users, userData, indent=4)
    else:
        # if it is empty the 'user' dict is added to the json file in a list by itself
        with open("userData.json", 'w') as userData:
            json.dump([user], userData, indent=4)

    return True, username


# method to log in to an existing user account
def login():
    # cleans the terminal and prints the screen tittle
    os.system('cls')
    print("------Login to your account------\n")
    # fail count that will keep track how many times user failed to log in
    fail_count = 0
    while fail_count < 5:
        # as long as the user haven't failed to log in for 5 times keep prompting for username and password
        username = input("Enter username: ")
        password = hash_password(input("Enter password: "))

        # this check if the userdata json file is empty and give an error message
        if os.path.getsize("userData.json") == 0:
            print("\nuser doesn't exist! create an account!\n")
            # then wait for 2 seconds
            time.sleep(2)
            # this help redirect the user to welcome screen
            return False, None

        # this will run if the json file is not empty
        with open("userData.json", "r") as userJson:
            # comparing username input with all the users in the json file
            for user in json.load(userJson):
                # if the username input match with one of the users
                if username == user["username"]:
                    # the input password will be matched with password belonging to that user
                    if password == user["password"]:
                        # if the password also matches returning true signals a successful login
                        # and the username returned to use in tasks manager screen
                        return True, username
            # if the loop exited without matching either username or password this message prints
            print("invalid username/password, please try again!")
            # failed login attempts are counted
            fail_count += 1

    # when login failed for the sixth time returning false
    return False, None


# used when creating a new user to see if the username already exists
def valid_user(username):
    # if the json file is empty any username is available, so it returns true
    if os.path.getsize("userData.json") == 0:
        return True
    else:
        # if the file is not empty we go through all users' usernames
        with open("userData.json", 'r') as userData:
            users = json.load(userData)
            for user in users:
                # if username is in the json file, return false
                # signalling that the username new user entered is not available
                if username == user["username"]:
                    return False
                else:
                    # if didn't match loop will continue
                    continue
            # if none of the usernames matched it will return true
            # saying that the username new user entered is available
            return True


if __name__ == "__main__":
    login()
