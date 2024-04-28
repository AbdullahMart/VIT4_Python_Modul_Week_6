from abc import ABC, abstractmethod
from datetime import datetime

class Task(ABC):
    def __init__(self, title, deadline):
        self.title = title
        self.deadline = deadline
        self.completed = False

    @abstractmethod
    def display_info(self):
        pass

class PersonalTask(Task):
    def __init__(self, title, deadline, priority):
        super().__init__(title, deadline)
        self.priority = priority

    def display_info(self):
        status = "Completed" if self.completed else "Not Completed"
        print(f"Title: {self.title}, Deadline: {self.deadline}, Priority: {self.priority}, Status: {status}")

class WorkTask(Task):
    def __init__(self, title, deadline, project):
        super().__init__(title, deadline)
        self.project = project

    def display_info(self):
        status = "Completed" if self.completed else "Not Completed"
        print(f"Title: {self.title}, Deadline: {self.deadline}, Project: {self.project}, Status: {status}")

class TaskManagement:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def display_tasks(self):
        for task in self.task_list:
            task.display_info()

# Örnek kullanım
if __name__ == "__main__":
    task_manager = TaskManagement()

    personal_task = PersonalTask("Go to the dentist", datetime(2024, 4, 30), "High")
    work_task = WorkTask("Finish project report", datetime(2024, 5, 10), "Project X")

    task_manager.add_task(personal_task)
    task_manager.add_task(work_task)

    task_manager.display_tasks()