# todo_list program

todo_list = []

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Task added.")

def view_tasks():
    if not todo_list:
        print("No tasks to display.")
    else:
        print("Your tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def remove_task():
    if not todo_list:
        print("No tasks to remove.")
    else:
        view_tasks()
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(todo_list):
                removed_task = todo_list.remove(task_number - 1)
                print(f'Task "{removed_task}" removed.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

while True:
    user_action = input("\nWrite a command (add, view, remove, exit): ").lower()

    if user_action == "add":
        add_task()
    elif user_action == "view":
        view_tasks()
    elif user_action == "remove":
        remove_task()
    elif user_action == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid command.")