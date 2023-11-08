
if __name__ == '__main__':
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

    match userinput:
        case 1:
            pass
        case 2:
            pass
        case 3:
            exit()
        case _:
            print("an error occurred in match case statement..!")
