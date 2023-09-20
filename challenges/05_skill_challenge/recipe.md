Single-Class Programs Design Recipe
1. Describe the Problem
> As a user
> So that I can keep track of my tasks
> I want a program that I can add todo tasks to and see a list of them.

> As a user
> So that I can focus on tasks to complete
> I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface
The interface of a class includes:

class TaskManager:

def __init__(self):
    Params:
        None
    Returns:
        none

def add(self, task):
    Params:
        task as a string
    Returns:
        None


def list_tasks():
    Params:
        None
    Returns:
        all tasks not completed

def delete(task):
    Params:
        task as a string
    Returns:
        None         


3. Create Examples as Tests

Check that a task is added
    task_manager = TaskManager()
    task_manager.add_task('Do laundry')
    task_manager.show_list() ==> 'Do laundry'

Check that another task can be added
    task_manager = TaskManager()
    task_manager.add_task('Do laundry')
    task_manager.add_task('Wash up')
    task_manager.show_list() ==> 'Do laundry, Wash up'
    

Check that a task is marked as complete by deleting
    task_manager = TaskManager()
    task_manager.add_task('Do laundry')
    task_manager.add_task('Wash up')
    task_manager.delete_task('Do laundry')
    task_manager.show_list() ==> 'Wash up'

Check that when there are no tasks, a message shows
    task_manager = TaskManager()
    task_manager.add_task('Do laundry')
    task_manager.delete_task('Do laundry')
    task_manager.tshow_list() ==> 'No tasks'

Check that a lowercase task can be deleted
    task_manager = TaskManager()
    task_manager.add_task('Do laundry')
    task_manager.delete_task('do laundry')
    task_manager.show_list() ==> 'No tasks'

Check that an uppercase task can be deleted
    task_manager = TaskManager()
    task_manager.add_task('Do laundry')
    task_manager.delete_task('DO laundry')
    task_manager.show_list() ==> 'No tasks'


4. Implement the Behaviour
