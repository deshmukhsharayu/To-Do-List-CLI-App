import sys
import os

TODO_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        f.write("\n".join(tasks))

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found!")
    else:
        print("\n📌 To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Removed: {removed}")
    except IndexError:
        print("⚠️ Invalid task number.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add/list/remove] [task]")
        return

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) >= 3:
            task = " ".join(sys.argv[2:])
            add_task(task)
        else:
            print("⚠️ Please provide a task to add.")
    elif command == "list":
        list_tasks()
    elif command == "remove":
        if len(sys.argv) == 3 and sys.argv[2].isdigit():
            remove_task(int(sys.argv[2]))
        else:
            print("⚠️ Please provide a valid task number to remove.")
    else:
        print("⚠️ Unknown command.")

if __name__ == "__main__":
    main()
