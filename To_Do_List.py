"""Project 2: To-Do List Application 
1. Project Overview: 
You are required to develop a Python program that acts as a basic to-do list system. The 
program should continuously prompt the user to either add new tasks, view current tasks, 
or delete existing tasks until the user decides to exit the application. 
"""

"""2. Functionalities to Implement: 
1. Add Task (add_task): 
o Function to add a new task to the to-do list. 
o Each task will be a string, and it will be stored in a list. """

def add_task(tasks):
    #asks for task and add to the list
    task = input("Enter the task: ").strip()


    # Don't allow empty tasks
    if task == " ":
        print("Task cannot be empty.")
    else: 
        tasks.append(task)
        print("Task added")

def view_tasks(tasks):
    #shows all tasks along with their index
    if len(tasks) == 0:
        print("No tasks")
    else:
        print("\nYour tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

def delete_task(tasks):
    #delete task based on the index
    if len(tasks) == 0:
        print("No task to delete")
        return

    view_tasks(tasks)
    choice = input("Enter the task number to delete: ").strip()

    #validate: must be a number
    if not choice.isdigit():
        print("Invalid index! Please enter a number.")
        return

    index = int(choice)

    #validate: must be within the list range
    if index < 1 or index > len(tasks):
        print("Invalid index! No such tasks")
    else:
        removed = tasks.pop(index - 1)
        print(f"Deleted: {removed}")


def main():

    tasks = [] #list to store all tasks

    while True:
        print("\n--- To-Do List ---")
        print("1. Add task")
        print("2. view task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("You exited.")
            break
        else:
            print("Invalid choice! enter 1, 2, 3 or 4.")


main()