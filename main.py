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
                    # [1] is for login to existing user
                    case 1:
                        result, user = userManager.login()
                        if not result:
                            os.system('cls')
                            print("!! login failed !!\n")
                            welcome_screen()
                            continue
                        else:
                            taskManager.manager_menu(user)
                            break
                    case 2:
                        result, user = userManager.new_user()
                        if result:
                            taskManager.manager_menu(user)
                            break
                        else:
                            os.system('cls')
                            print("!! user not created !!\n")
                            welcome_screen()
                            continue
                    case 3:
                        os.system('cls')
                        exit()

                    case _:
                        os.system('cls')
                        print("Unknown option number!! "
                              "Enter the number in front of the action you want to perform..\n")
                        welcome_screen()
                        continue
            # if it's not a number error message is printed and loop continue to prompt input
            except ValueError:
                print("Invalid Input! only enter a number..")


if __name__ == '__main__':
    welcome()
