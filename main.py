# todo: add comments to the code, update and delete methods left to build
import userManager
import taskManager
import os


# Print welcome screen
def welcome_screen():
    print("-----Welcome to To Do List Manager-----\n")
    print("Select one of the options below:")
    print("[1] Login \n[2] Sign Up \n[3] Quit\n")


# welcome screen is displayed using welcome_screen() method,
# in this method and prompts the user to enter menu option number,
# it then validated and returned
def welcome():
    while True:
        # Display menu
        os.system('cls')
        welcome_screen()
        # loop keep going until a valid input is entered
        while True:
            # tyr block ensure the input is a number
            try:
                userinput = int(input("enter number:> "))
                # checks if the number entered is within the valid menu options
                match userinput:
                    # [1] in welcome menu, login to existing user
                    case 1:
                        # result let know if the log in successful or not
                        result, user = userManager.login()
                        if result:
                            # if log in successful redirect to the task manager menu
                            taskManager.manager_menu(user)
                            break
                        else:
                            # if login failed, print a message then print welcome menu again
                            os.system('cls')
                            print("!! login failed !!\n")
                            welcome_screen()
                            # continue to the start of this loop and prompt user input
                            continue

                    # [2] in welcome menu, create new user
                    case 2:
                        # result tells if the new user created successfully or not
                        result, user = userManager.new_user()
                        if result:
                            # if user created, redirects to task manager menu
                            taskManager.manager_menu(user)
                            break
                        else:
                            # if user not created message is printed, then the welcome menu
                            os.system('cls')
                            print("!! user not created !!\n")
                            welcome_screen()
                            continue
                    # [3] in welcome menu, quit the app
                    case 3:
                        # clears the screen and exits the app
                        os.system('cls')
                        exit()
                    # when a number entered that is invalid menu option number
                    case _:
                        # prints the message to enter correct number
                        os.system('cls')
                        print("Unknown option number!! "
                              "Enter the number in front of the action you want to perform..\n")
                        # prints the welcome menu and continue to the start of loop
                        welcome_screen()
                        continue
            # if it's not a number error message is printed and loop continue to prompt input
            except ValueError:
                print("Invalid Input! only enter a number..")


if __name__ == '__main__':
    welcome()
