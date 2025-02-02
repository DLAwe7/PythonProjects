print("Welcome to your To-Do List manager!")
options = ["1. Add a new task", "2. View all tasks", "3. Mark a task as done", "4. Exit"]

tasks_list = []
while True:
    print("Choose and option: ")
    for option in options:
        print(option)
    user_input = input("> ")

    if user_input == "1":
        print(f"Your choice: {user_input}")
        new_task = input("Enter the new task: ").lower()
        tasks_list.append(new_task)
        print("Done!")
        print()

    elif user_input == "2":
        print(f"Your choice: {user_input}")
        print(tasks_list)
        print()
    elif user_input == "3":
        print(f"Your choice: {user_input}")
        task_remover = input("Enter the task to be removed: ").lower()
        if task_remover in tasks_list:
            tasks_list.remove(task_remover)
            print(f"Task {task_remover} removed from list! ")
            print()
        else:
            print(f"{task_remover} is not within your tasks list")
            print()
    elif user_input == "4":
        print("Goodbye!")
        break
    else:
        print("Input is not valid. Please choose from numbers 1-4")
        print()
