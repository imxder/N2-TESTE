class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def mark_task_done(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.done = True
                break

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                break