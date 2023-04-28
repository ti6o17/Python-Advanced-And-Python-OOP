from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {Task.details(new_task)} is added to the section"

    def complete_task(self, task_name: str):
        if task_name in self.tasks:
            Task.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        num_tasks = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                num_tasks += 1
        return f"Cleared {num_tasks} tasks."

    def view_section(self):
        result = ""
        result += f"Section {self.name}:"
        for task in self.tasks:
            result += '\n' + task.details()
        return result

