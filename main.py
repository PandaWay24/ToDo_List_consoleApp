# todo: add comments to the code, taskManager view, update and delete methods left to build
import userManager
import taskManager
import os


# welcome screen is displayed in this method and prompts the user to enter menu option number,
# it then validated and returned
def welcome():
    # Display menu
    os.system('cls')
    print("-----Welcome to To Do List Manager-----\n")
    print("Select one of the options below:")
    print("[1] Login \n[2] Sign Up \n[3] Quit\n")
    # loop keep going until a valid input is entered
    while True:
        # tyr block ensure the input is a number
        try:
            userinput = int(input("enter number:> "))
            # checks if the number entered is within the valid menu options
            if userinput in [1, 2, 3]:
                break
            else:
                print("Unknown option number!! Enter the number in front of the action you want to perform..")
                continue
        # if it's not a number error message is printed and loop continue to prompt input
        except ValueError:
            print("Invalid Input! only enter a number..")

    return userinput


# match the user input for task manager menu with the appropriate action
def task_manage(menu_option, logged_username):
    match menu_option:
        # menu option 1 is to add tasks
        case 1:
            result = taskManager.add(logged_username)
            # results tells if the task adding was successful or not
            if result:
                while True:
                    # looping through as long as user want to add more tasks
                    add_more = input("\nContinue adding tasks? (y/n): ")
                    if add_more.lower() == "y":
                        result = taskManager.add(logged_username)
                    elif add_more.lower() == "n":
                        # this takes out of the loop to add and take the user to task managing menu
                        # false keep the task manager menu going
                        return False
                    else:
                        # prints an error message when the input is neither "y" nor "n",
                        # then loop back to input prompt
                        print("Invalid input!! Try again!!")
                        continue
            else:
                # if for unforeseen reason adding task returned false
                print("adding tasks unsuccessful!!")
        case 2:
            # menu option 2, to view the tasks list
            taskManager.view(username)
        case 3:
            # menu option 3, to update the task list
            pass
        case 4:
            # menu option 4, to delete a task from the list
            pass
        case 5:
            # this is used to exit the task manager menu and return to welcome screen
            return True
        case _:
            # even though menu option inputs are validated this is here as a safeguard to
            # any unforeseen error!
            print("Invalid Input! only enter a number..")

    return False


if __name__ == '__main__':
    while True:
        match welcome():
            case 1:
                logged, username = userManager.login()
                if not logged:
                    continue
                else:
                    while True:
                        option = taskManager.manager_menu(username)
                        if option:
                            logout = task_manage(option, username)
                            if logout:
                                break
                            else:
                                continue
                        else:
                            print("Error!! Option returned False!!")

            case 2:
                logged, username = userManager.new_user()
                if logged:
                    option = taskManager.manager_menu(username)
                    if option:
                        task_manage(option, username)
                    else:
                        print("Error!! Option returned False!!")
                else:
                    print("User not created!!")
                    continue

            case 3:
                exit()

            case _:
                print("an error occurred in match case statement..!")
