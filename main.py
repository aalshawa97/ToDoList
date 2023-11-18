class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task['name']} - Due: {task.get('due_date', 'N/A')} - Priority: {task.get('priority', 'N/A')}")

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


# Example Usage:
if __name__ == "__main__":
    todo_list = ToDoList()

    #todo_list.add_task({'name': 'Complete Project', 'due_date': '2023-12-01', 'priority': 'High'})
    #todo_list.add_task({'name': 'Study for Exam', 'due_date': '2023-11-30', 'priority': 'Medium'})
    todo_list.add_task({'name': 'Pray', 'due_date': 'N/A', 'priority': 'High'})
    #todo_list.add_task({'name': '2023-11-30', 'due_date': 'N/A', 'priority': 'High'})


    todo_list.view_tasks()

    todo_list.mark_as_complete(1)

    #todo_list.remove_task(2)

    #todo_list.view_tasks()
