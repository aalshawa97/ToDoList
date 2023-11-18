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
            task_number = input('Task number to be removed?\n')
            todo_list.remove_task(int(task_number))
        if option == 'q':
            'Exiting program'
            return

# Example Usage:
if __name__ == "__main__":
    todo_list = ToDoList()

    userMessage = ' '
    #Do while in Python
    while True:
        #Ask user
        # Menu
        userInput = input('a to add a task\n'
                          'c to mark a task as complete\n'
                          'r to remove a task\n'
                          'q to quit\n')
        userMessage = ToDoList.menu(userInput)
        if userInput == 'q':
            break



    #todo_list.add_task({'name': 'Complete Project', 'due_date': '2023-12-01', 'priority': 'High'})
    #todo_list.add_task({'name': 'Study for Exam', 'due_date': '2023-11-30', 'priority': 'Medium'})
    #todo_list.add_task({'name': '2023-11-30', 'due_date': 'N/A', 'priority': 'High'})


    todo_list.view_tasks()
    print('Thank you for using the to-do task application, goodbye.')

    #todo_list.mark_as_complete(1)

    #todo_list.remove_task(2)

    #todo_list.view_tasks()
