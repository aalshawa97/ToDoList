import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"{task.get('name')} Added")

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task['name']} - Due: {task.get('due_date', 'N/A')} - Priority: {task.get('priority', 'N/A')} - {'(Completed)' if task.get('complete', False) else ''}")

    def mark_as_complete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['complete'] = True
            print(f"Task '{self.tasks[task_index - 1]['name']}' marked as complete.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task['name']}' removed.")
        else:
            print("Invalid task index.")

    @staticmethod
    def menu(option):
        if option == 'a':
            name = input('Task name?\n')
            due_date = input('Task due when?\n')
            priority = input('Task priority?\n')
            todo_list.add_task({'name': name, 'due_date': due_date, 'priority': priority})
            return "Task added"
        if option == 'c':
            task_number = input('Task number completed?\n')
            todo_list.mark_as_complete(int(task_number))
        if option == 'r':
            task_number = input('Task number to remove?\n')
            todo_list.remove_task(int(task_number))
        if option == 'q':
            print('Exiting program')
            return

def on_add_task():
    name = entry_name.get()
    due_date = entry_due_date.get()
    priority = entry_priority.get()
    todo_list.add_task({'name': name, 'due_date': due_date, 'priority': priority})
    update_task_list()

def on_mark_as_complete():
    try:
        task_number = int(entry_task_number.get())
        todo_list.mark_as_complete(task_number)
        update_task_list()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid task number.")

def on_remove_task():
    try:
        task_number = int(entry_remove_task_number.get())
        todo_list.remove_task(task_number)
        update_task_list()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid task number.")

def update_task_list():
    task_list.delete(1.0, tk.END)
    if todo_list.tasks:
        for index, task in enumerate(todo_list.tasks, start=1):
            completed_text = "(Completed) " if task.get('complete', False) else ""
            task_list.insert(tk.END, f"{index}. {completed_text}{task['name']} - Due: {task.get('due_date', 'N/A')} - Priority: {task.get('priority', 'N/A')}\n")
    else:
        task_list.insert(tk.END, "No tasks")

# Example Usage:
if __name__ == "__main__":
    todo_list = ToDoList()

    root = tk.Tk()
    root.title("To-Do List Application")

    label_name = tk.Label(root, text="Task Name:")
    label_name.pack()

    entry_name = tk.Entry(root)
    entry_name.pack()

    label_due_date = tk.Label(root, text="Due Date:")
    label_due_date.pack()

    entry_due_date = tk.Entry(root)
    entry_due_date.pack()

    label_priority = tk.Label(root, text="Priority:")
    label_priority.pack()

    entry_priority = tk.Entry(root)
    entry_priority.pack()

    btn_add_task = tk.Button(root, text="Add Task", command=on_add_task)
    btn_add_task.pack()

    label_task_number = tk.Label(root, text="Task Number:")
    label_task_number.pack()

    entry_task_number = tk.Entry(root)
    entry_task_number.pack()

    btn_mark_as_complete = tk.Button(root, text="Mark as Complete", command=on_mark_as_complete)
    btn_mark_as_complete.pack()

    label_remove_task_number = tk.Label(root, text="Task Number to Remove:")
    label_remove_task_number.pack()

    entry_remove_task_number = tk.Entry(root)
    entry_remove_task_number.pack()

    btn_remove_task = tk.Button(root, text="Remove Task", command=on_remove_task)
    btn_remove_task.pack()

    task_list = tk.Text(root, height=10, width=50)
    task_list.pack()

    update_task_list()

    root.mainloop()
