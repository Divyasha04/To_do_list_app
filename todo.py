# To-Do List App using CLI

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print("\n✨ To-Do List ✨")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks(tasks):
    if tasks:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\n📭 No tasks yet!")

def add_task(tasks):
    task = input("➕ Enter new task: ").strip()
    if task:
        tasks.append(task)
        print("✅ Task added!")
    else:
        print("⚠️ Empty task not added.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("❌ Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"✅ Removed: {removed}")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("🔘 Choose (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("💾 Tasks saved!")
            break
        else:
            print("⚠️ Invalid choice")

if __name__ == "__main__":
    main()
