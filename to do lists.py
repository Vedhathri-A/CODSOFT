Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def display_menu():
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
...     print("Task added successfully!")
... 
... def view_tasks(tasks):
...     print("Current Tasks:")
...     for i, task in enumerate(tasks, start=1):
...         status = "✓" if task.startswith("✓") else "✗"
...         print(f"{i}. {status} {task[2:]}")
... 
... def mark_complete(tasks):
...     view_tasks(tasks)
...     task_num = int(input("Enter the number of the task to mark as complete: "))
...     if task_num < 1 or task_num > len(tasks):
...         print("Invalid task number.")
...         return
...     task = tasks[task_num - 1]
...     if task.startswith("✓"):
...         print("Task is already complete.")
...     else:
...         tasks[task_num - 1] = "✓ " + task
...         print("Task marked as complete.")
... 
... def main():
...     tasks = []
...     while True:
...         display_menu()
...         choice = input("Enter your choice (1-4): ")
...         if choice == "1":
...             add_task(tasks)
...         elif choice == "2":
...             view_tasks(tasks)
...         elif choice == "3":
...             mark_complete(tasks)
...         elif choice == "4":
...             print("Exiting to-do list...")
...             break
...         else:
...             print("Invalid choice. Please try again.")
... 
... if __name__ == "__main__":
