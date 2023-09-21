import pytest
from lib.todo import *

def test_todo_returns_correct_task():
    todo = Todo('Do laundry')

    assert todo.task == 'Do laundry'

def test_todo_returns_string():
    with pytest.raises(Exception) as e:
        Todo(5)
    error_message = str(e.value)
    assert error_message == 'Task must be a string'

def test_initial_todo_complete_is_false():
    todo = Todo('Do laundry')

    assert todo.complete == False

def test_mark_complete_changes_to_True():
    todo = Todo('Do laundry')

    todo.mark_complete()
    
    assert todo.complete == True