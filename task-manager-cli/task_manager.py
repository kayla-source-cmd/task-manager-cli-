tasks = []

def show_menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append({"name": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Pending"
        print(i, task["name"], "-", status)

def complete_task():
    view_tasks()
    number = int(input("Enter task number: "))
    tasks[number - 1]["completed"] = True
    print("Task completed!") 

def delete_task():
    view_tasks()
    number = int(input("Enter task number to delete: "))
    tasks.pop(number - 1)
    print("Task deleted!")         

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")