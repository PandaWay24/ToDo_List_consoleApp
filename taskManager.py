# Methods to manage the tasks in to do list
import json
import os
import re


def manager_menu(username):
    print(f"Hello {username}, What would you like to do today?\n")
    print("[1] Add a new task \n[2] View my tasks list \n[3] Update a task \n[4] Delete a task\n-----\n[5] Log Out\n")

    option = False

    while True:
        try:
            option = int(input("Enter number: "))
            break

        except ValueError:
            print("Invalid Input! only enter a number..")
            continue

    return option


def add(username):
    print("------Adding a new task------")
    print("*Title cannot be empty, leave other info empty if you want to add later!")
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
            if re.search("^\d\d/\d\d/\d\d\d\d$", due):
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

    view(username)
    return True



def view(username):
    with open("taskData.json", "r") as taskJson:
        user_tasks = json.load(taskJson)[username]
        print(user_tasks)


def update():
    pass


def delete():
    pass
