from datetime import datetime

class Task:
    all_tasks = []  # переменная класса, список для хранения всех задач

    def __init__(self, description, deadline, status='open'):
        self.description = description  # описание задачи
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")  # срок выполнения
        self.status = status
        Task.all_tasks.append(self)  # добавляем задачу в общий список при создании

    def add_task(self, description, deadline, status='open'):
        new_task = Task(description, deadline, status)
        return new_task

    def mark_done(self):
        self.status = "done"

    def show_open_task(self):
        print("Open tasks:")
        for task in Task.all_tasks:
            if task.status == "open":
                print(f"- {task.description} (before {task.deadline.date()})")

    def show_all_tasks(self):
        print("All Tasks:")
        for task in Task.all_tasks:
            print(f"- {task.description} (before {task.deadline.date()}), status: {task.status}")

Task1 = Task("make dinner", "2025-01-05", "open")
Task2 = Task("wash the dish", "2025-01-06", "open")
Task3 = Task("turn off the light", "2025-04-27", "open")

Task1.show_all_tasks()
print()