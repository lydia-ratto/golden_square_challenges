class TaskManager:

    def __init__(self):
        self.task_list = []
    
    def add_task(self, task):
        self.task_list.append(task.lower().capitalize())
    
    def delete_task(self, task):
        self.task_list.remove(task.lower().capitalize())

    def show_list(self):
        if self.task_list == []:
            return 'No tasks'
        return ', '.join(self.task_list)