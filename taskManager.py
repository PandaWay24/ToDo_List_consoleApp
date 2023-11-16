# Methods to manage the tasks in to do list
import json
import re
import os


# prints the task managing menu and redirect to the action user chose
def manager_menu(username):
    # this loop keep the task manager menu going so user can
    # return here after performing one action
    while True:
        # clear the screen and prints the menu
        os.system('cls')
        print(f"Hello {username}, What would you like to do today?\n")
        print(
            "[1] Add a new task \n[2] View my tasks list \n[3] Update a task \n[4] Delete a task\n-----\n[5] Log Out\n")
        # try block ensure the user only enters a number
        try:
            option = int(input("Enter number: "))

        except ValueError:
            print("Invalid Input! only enter a number..")
        # when try block was successful following code evaluates the user input
        else:
            match option:
                # [1] to add new tasks
                case 1:
                    # results makes sure task adding were successful
                    result = add(username)
                    # if it is successful
                    if result:
                        while True:
                            # looping through as long as user want to add more tasks
                            add_more = input("\nContinue adding tasks? (y/n): ")
                            if add_more.lower() == "y":
                                result = add(username)
                            elif add_more.lower() == "n":
                                # this takes out of the loop to add and take the user to task managing menu
                                break
                            else:
                                # prints an error message when the input is neither "y" nor "n",
                                # then loop back to input prompt, for add_more
                                print("Invalid input!! Try again!!")
                                continue
                    else:
                        # this is unlikely to happen, help to troubleshoot if anything happened
                        print("adding tasks unsuccessful!!")
                # [3] to view tasks
                case 2:
                    # when viewing tasks at first this avoids any filtering
                    tags = None
                    # loop keep going to allow the user to add and remove filters until they are done
                    while True:
                        # got_tasks tells if the user currently have added any tasks or not
                        got_tasks = view(username, tags)
                        # if there are tasks they will be printed from 'view' method
                        if got_tasks:
                            # after tasks have printed, this prompt ask whether to return to menu or
                            # filter by tags or remove any filters
                            while True:
                                view_option = input("[ok] if done viewing, [f] to filter by tag, "
                                                    "[x] to remove filters: ").lower()
                                # keep the loop going until the input is valid, then break
                                if view_option not in ["ok", "f", "x"]:
                                    print("Invalid input!! please try again!!")
                                    continue
                                else:
                                    break
                        else:
                            # if there are no tasks in saved under current user,
                            # view method return false without printing anything
                            print("You currently don't have any task, Try adding tasks first!!")
                            # this is used to keep the app from returning to the task manager menu,
                            # until user acknowledges the message, afterwords returns to tasks manager
                            input("Press [enter] to return to task menu: ")
                            break

                        # this block maps the input to relevant action
                        if view_option == "ok":
                            break
                        elif view_option == "f":
                            # prompt to enter tags separated by commas (,)
                            tags = input("Enter tag/s you want to filter by (separate with commas ','): ").split(',')
                            # user may add unnecessary spaces when entering tag names
                            # this statement uses .strip() string method on each individual tag name to remove spaces
                            # at the start and end of each tag name
                            tags = [t.strip() for t in tags]
                            continue
                        elif view_option == "x":
                            # this remove tags that previously been applied
                            tags = None
                            continue
                case 3:
                    update(username)
                case 4:
                    delete(username)
                case 5:
                    return
                case _:
                    print("Invalid number!! only enter the number of the menu option you want!")


# method to add new tasks to users tasks list
def add(username):
    # screen cleared and screen title is printed
    os.system('cls')
    print("------Adding a new task------\n")
    # informs the user that every task must have a tittle, while other things can be updated later
    print("*Title is required, leave other info empty if you want to add later!\n")
    # this loop ensure that title is not empty
    while True:
        title = input("Enter task Title: ")

        if not title.strip():
            print("Task Title cannot be empty!! Try Again!!")
            continue
        else:
            break
    # prompt for task description
    description = input("Enter Description: ")

    # this loop ensure that date is entered in 'dd/mm/yyyy' pattern
    while True:
        due = input("Enter Due Date (dd/mm/yyyy): ").strip()

        # as due date can be left empty this block only match the pattern if the due date is not left empty
        if due:
            # return true if the pattern is matched. if matched breaks out of the loop
            if re.search('^\d\d/\d\d/\d\d\d\d$', due):
                break
            else:
                # if pattern didn't match prints the message and continue loop to prompt for a due date
                print("Invalid Format!! use this format with digits: dd/mm/yyyy")
                continue
        else:
            # if the due date is left empty, breaks the loop to continue to the next input (tags)
            break
    # tags are split by a comma
    tags = input("Enter Tags (separate with commas): ").split(',')
    # remove spaces from start and end of each tag and update the tags list
    tags = [t.strip() for t in tags]

    # python dict to save in json file
    # ID is set to 1, this is used if there are no previous tasks under current user
    task = {"ID": 1, "Title": title, "Description": description, "Due Date": due, "Tags": tags}

    # if the tasks data file is empty reading it will cause errors
    # this if block saves the task with current user's username in the empty file
    if os.path.getsize("taskData.json") == 0:
        with open("taskData.json", "w") as taskJson:
            json.dump([{username: [task]}], taskJson, indent=4)

    # if json file is not empty
    else:
        # json file have username as key and list of task dicts as their value
        with open("taskData.json", "r") as taskJson:
            users = json.load(taskJson)

        # to see if the username is in the json file
        for user in users:
            if username in user.keys():
                user_index = users.index(user)
                # getting all tasks under current user
                user_tasks = users[user_index][username]
                # implementing task ID by adding one to the last task's ID in user's tasks list
                task['ID'] = user_tasks[-1]['ID'] + 1

                # Task with new task ID is added to the user's tasks list and written in json file
                with open("taskData.json", "w") as taskJson:
                    json.dump([users[user_index][username] + [task]], taskJson, indent=4)
        # this runs if the username is not in the taskData.json,
        # which means there are no previously saved tasks under current user
        else:

            with open("taskData.json", "w") as taskJson:
                json.dump(users + [{username: [task]}], taskJson, indent=4)

    print("\nFollowing task has been added successfully:\n")
    print_task(task)

    return True


def view(username, tags=None):
    os.system('cls')
    with open("taskData.json", "r") as taskJson:
        try:
            users = json.load(taskJson)
            # print(users)
            for user in users:
                # print(user)
                if username in user.keys():
                    # print(user.keys())
                    user_index = users.index(user)
                    break
            user_tasks = users[user_index][username]

        except KeyError:
            print(KeyError)
            return False

    count = 0
    if not tags:
        for task in user_tasks:
            count += 1
            print_task(task)
    else:
        for task in user_tasks:
            count += 1
            if all(tag in task['Tags'] for tag in tags):
                print_task(task)

    return True


def update():
    pass


def delete():
    pass


def print_task(task):
    print(f"      Title: {task['Title']}\n"
          f"Description: {task['Description']}\n"
          f"   Due Date: {task['Due Date']}\n"
          f"       Tags: {task['Tags']}\n")


if __name__ == "__main__":
    x = view("ddd")
    print(x)
