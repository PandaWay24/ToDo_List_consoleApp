# todo: add comments to the code, fix the issue in login method
import userManager
import taskManager


def welcome():
    print("-----Welcome to To Do List Manager-----\n")
    print("Select one of the options below:")
    print("[1] Login \n[2] Sign Up \n[3] Quit\n")

    while True:
        try:
            userinput = int(input("enter number:> "))
            if userinput in [1, 2, 3]:
                break
            else:
                print("Unknown option number!! Enter the number in front of the action you want to perform..")
                continue

        except ValueError:
            print("Invalid Input! only enter a number..")

    return userinput


def task_manage(menu_option, logged_username):
    match menu_option:
        case 1:
            result = taskManager.add(logged_username)
            if result:
                taskManager.view(username)
                while True:
                    add_more = input("\nContinue adding tasks (y/n): ")
                    if add_more.lower() == "y":
                        result = taskManager.add(logged_username)
                    elif add_more.lower() == "n":
                        return False
                    else:
                        print("Invalid input!! Try again!!")
                        continue
            else:
                print("adding tasks unsuccessful!!")
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            return True
        case _:
            print("error!! option didn't match!!!")

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
