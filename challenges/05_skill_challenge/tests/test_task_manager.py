from lib.task_manager import *

def test_task_added():
    task_manager = TaskManager()
    task_manager.add_task('Do laundry')
    assert task_manager.show_list() == 'Do laundry'

def test_second_task_added():
    task_manager = TaskManager()
    task_manager.add_task('Do laundry')
    task_manager.add_task('Wash up')
    assert task_manager.show_list() == 'Do laundry, Wash up'


def test_no_tasks_message():
    task_manager = TaskManager()
    assert task_manager.show_list() == 'No tasks'

def test_task_deleted():
    task_manager = TaskManager()
    task_manager.add_task('Do laundry')
    task_manager.add_task('Wash up')
    task_manager.delete_task('Wash up')
    assert task_manager.show_list() == 'Do laundry'


def test_uppercase_task_deleted():
    task_manager = TaskManager()
    task_manager.add_task('Do laundry')
    task_manager.add_task('Wash up')
    task_manager.delete_task('WASH up')
    assert task_manager.show_list() == 'Do laundry'

def test_lowercase_task_deleted():
    task_manager = TaskManager()
    task_manager.add_task('Do laundry')
    task_manager.add_task('Wash up')
    task_manager.delete_task('wash up')
    assert task_manager.show_list() == 'Do laundry'