# Methods to manage the tasks in to do list
import json
import re
import os


def manager_menu(username):
    while True:
        os.system('cls')
        print(f"Hello {username}, What would you like to do today?\n")
        print(
            "[1] Add a new task \n[2] View my tasks list \n[3] Update a task \n[4] Delete a task\n-----\n[5] Log Out\n")

        try:
            option = int(input("Enter number: "))

        except ValueError:
            print("Invalid Input! only enter a number..")

        else:
            match option:
                case 1:
                    result = add(username)
                    if result:
                        while True:
                            # looping through as long as user want to add more tasks
                            add_more = input("\nContinue adding tasks? (y/n): ")
                            if add_more.lower() == "y":
                                result = add(username)
                            elif add_more.lower() == "n":
                                # this takes out of the loop to add and take the user to task managing menu
                                # false keep the task manager menu going
                                break
                            else:
                                # prints an error message when the input is neither "y" nor "n",
                                # then loop back to input prompt
                                print("Invalid input!! Try again!!")
                                continue
                    else:
                        # if for unforeseen reason adding task returned false
                        print("adding tasks unsuccessful!!")
                case 2:
                    tags = None
                    while True:
                        view(username, tags)
                        view_option = input("[ok] if done viewing, [f] to filter by tag, [x] to remove filters: ").lower()
                        if view_option == "ok":
                            break
                        elif view_option == "f":
                            tags = input("Enter tag/s you want to filter by (separate with commas ','): ").split(',')
                            continue
                        elif view_option == "x":
                            tags = None
                            continue
                        else:
                            print("Invalid Input!! enter 'ok' or 'f' or 'x' and try again!")
                case 3:
                    update(username)
                case 4:
                    delete(username)
                case 5:
                    return
                case _:
                    print("Invalid number!! only enter the number of the menu option you want!")


def add(username):
    os.system('cls')
    print("------Adding a new task------\n")
    print("*Title cannot be empty, leave other info empty if you want to add later!\n")
    while True:
        title = input("Enter task Title: ")

        if not title.strip():
            print("Task Title cannot be empty!! Try Again!!")
            continue
        else:
            break

    description = input("Enter Description: ")

    while True:
        due = input("Enter Due Date (dd/mm/yyyy): ")

        due = due.strip()

        if due:
            if re.search('^\d\d/\d\d/\d\d\d\d$', due):
                break
            else:
                print("Invalid Format!! use this format with digits: dd/mm/yyyy")
                continue
        else:
            break

    tags = input("Enter Tags (separate with commas): ")

    task = {"title": title, "description": description, "due date": due, "tags": tags.split(",")}

    if os.path.getsize("taskData.json") == 0:
        with open("taskData.json", "w") as taskJson:
            json.dump({username: [task]}, taskJson, indent=4)

    else:
        with open("taskData.json", "r") as taskJson:
            tasks = json.load(taskJson)

        if username in tasks.keys():
            user_tasks = tasks[username]
            with open("taskData.json", "w") as taskJson:
                json.dump({username: user_tasks + [task]}, taskJson, indent=4)
        else:
            with open("taskData.json", "w") as taskJson:
                json.dump({username: [task]}, taskJson, indent=4)

    print("\nFollowing task has been added successfully:")
    print_task(task)

    return True


def view(username, tags=None):
    os.system('cls')
    with open("taskData.json", "r") as taskJson:
        user_tasks = json.load(taskJson)[username]

    count = 0
    if not tags:
        for task in user_tasks:
            count += 1
            print_task(task)
    else:
        for task in user_tasks:
            count += 1
            for tag in tags:
                if tag in task['tags']:
                    print_task(task)


def update():
    pass


def delete():
    pass


def print_task(task):
    print(f"      Title: {task['title']}\n"
          f"Description: {task['description']}\n"
          f"   Due Date: {task['due date']}\n"
          f"       Tags: {task['tags']}\n")


if __name__ == "__main__":
    view("mmm")
