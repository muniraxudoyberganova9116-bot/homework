# To-Do Application

# Objective: Create a flexible To-Do application to manage tasks with support for different file storage formats (e.g., CSV, JSON). The application should be designed such that adding support for a new file format requires minimal changes to the code.
# Task Description
# 1. Functional Requirements:

# Your To-Do application should provide the following features:

#    1. Add a task: Allow users to add tasks with the following details:
#         Task ID
#         Title
#         Description
#         Due Date (optional)
#         Status (e.g., Pending, In Progress, Completed)
#     2. View tasks: Display all tasks with their details.
#     3. Update a task: Allow users to modify a task's details using its Task ID.
#     4. Delete a task: Remove a task by its Task ID.
#     5. Filter tasks: Filter tasks by status (e.g., Pending or Completed).
#     6. Save and load tasks: Save tasks to a file and load them from the file on startup.

# 2. Design Requirements:

#     Separation of Concerns:
#     Support for Multiple Formats:
#     Minimal Code Changes:
# 3. Example Usage:

# Welcome to the To-Do Application!
# 1. Add a new task
# 2. View all tasks
# 3. Update a task
# 4. Delete a task
# 5. Filter tasks by status
# 6. Save tasks
# 7. Load tasks
# 8. Exit

# Enter your choice: 1
# Enter Task ID: 101
# Enter Title: Finish Homework
# Enter Description: Complete math and science homework.
# Enter Due Date (YYYY-MM-DD): 2024-12-31
# Enter Status (Pending/In Progress/Completed): Pending
# Task added successfully!

# Enter your choice: 2
# Tasks:
# 101, Finish Homework, Complete math and science homework., 2024-12-31, Pending


class ToDoApp:
    def __init__(self, file_format='csv'):
        self.file_format = file_format
        self.tasks = []
        self.load_tasks()

    def add_task(self, task_id, title, description, due_date=None, status='Pending'):
        task = {
            'task_id': task_id,
            'title': title,
            'description': description,
            'due_date': due_date,
            'status': status
        }
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task['task_id'] == task_id:
                if title:
                    task['title'] = title
                if description:
                    task['description'] = description
                if due_date:
                    task['due_date'] = due_date
                if status:
                    task['status'] = status
                self.save_tasks()
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['task_id'] != task_id]
        self.save_tasks()

    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task['status'] == status]
        for task in filtered_tasks:
            print(task)
    def save_tasks(self):
        if self.file_format == 'csv':
            self.save_to_csv()
        elif self.file_format == 'json':
            self.save_to_json()
    def load_tasks(self):
        if self.file_format == 'csv':
            self.load_from_csv()
        elif self.file_format == 'json':
            self.load_from_json()
    def save_to_csv(self):
        import csv
        with open('tasks.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['task_id', 'title', 'description', 'due_date', 'status'])
            writer.writeheader()
            writer.writerows(self.tasks)
    def load_from_csv(self):
        import csv
        try:
            with open('tasks.csv', 'r') as file:
                reader = csv.DictReader(file)
                self.tasks = list(reader)
        except FileNotFoundError:
            self.tasks = []
    def save_to_json(self):
        import json
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)
    def load_from_json(self):
        import json
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = [] 
    def menu(self):
        while True:
            print("\nTo-Do Application")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                task_id = input("Enter Task ID: ")
                title = input("Enter Title: ")
                description = input("Enter Description: ")
                due_date = input("Enter Due Date (YYYY-MM-DD): ")
                status = input("Enter Status (Pending/In Progress/Completed): ")
                self.add_task(task_id, title, description, due_date, status)
                print("Task added successfully!")
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                task_id = input("Enter Task ID to update: ")
                title = input("Enter new Title (leave blank to keep current): ")
                description = input("Enter new Description (leave blank to keep current): ")
                due_date = input("Enter new Due Date (YYYY-MM-DD) (leave blank to keep current): ")
                status = input("Enter new Status (Pending/In Progress/Completed) (leave blank to keep current): ")
                self.update_task(task_id, title, description, due_date, status)
            elif choice == '4':
                task_id = input("Enter Task ID to delete: ")
                self.delete_task(task_id)
                print("Task deleted successfully!")
            elif choice == '5':
                status = input("Enter Status to filter by (Pending/In Progress/Completed): ")
                self.filter_tasks(status)
            elif choice == '6':
                self.save_tasks()
                print("Tasks saved successfully!")
            elif choice == '7':
                self.load_tasks()
                print("Tasks loaded successfully!")
            elif choice == '8':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again."   )

if __name__ == "__main__":
    app = ToDoApp(file_format='csv')  # Change to 'json' for JSON format
    app.menu()  