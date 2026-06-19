File_Name = "task.txt"

def load_tasks() :
    try:
        with open(File_Name, "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []
    
def save_tasks(tasks) :
    with open(File_Name, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(tasks: list) :
    task = input("Enter task description (or blank to cancel): ").strip()
    if not task:
        print("Add cancelled.")
        return
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def list_tasks(tasks: list) :
    if not tasks:
        print("No tasks.")
        return
    for i, t in enumerate(tasks, start=1):
         print(f"{i}. {t}")

def complete_task(tasks: list) :
    if not tasks:
        print("No tasks to complete.")
        return
    list_tasks(tasks)
    while True:
        choice = input("Enter the number of the task to mark complete (or 'done'): ").strip()
        if not choice:
            print("Please enter a value or type 'done'.")
            continue
        if choice.lower() in {"done", "cancel", "back"}:
            print("Complete cancelled.")
            return
        try:
            idx = int(choice)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if 1 <= idx <= len(tasks):
            completed = tasks.pop(idx - 1)
            save_tasks(tasks)
            print(f"Completed: {completed}")
            return
        print(f"Enter a number between 1 and {len(tasks)}.")

def edit_task(tasks: list) :
    if not tasks:   
        print("No tasks to edit.")
        return
    list_tasks(tasks)
    while True:
        choice = input("Enter the number of the task to edit (or 'done'): ").strip()
        if not choice:
            print("Please enter a value or type 'done'.")
            continue
        if choice.lower() in {"done", "cancel", "back"}:
            print("Edit cancelled.")
            return
        try:
            idx = int(choice)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if 1 <= idx <= len(tasks):
            new = input("Enter the new task description: ").strip()
            tasks[idx - 1] = new
            save_tasks(tasks)
            print("Task updated.")
            return
        print(f"Enter a number between 1 and {len(tasks)}.")

def main():
    tasks = load_tasks()
    while True:
        print("\nMenu:")
        print("1. List tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Edit task")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")



if __name__ == "__main__":
    main()
    