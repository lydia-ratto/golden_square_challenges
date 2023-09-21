from lib.todo import *
from lib.todo_list import *

def test_initial_todo_list_creates_empty_list():
    list = TodoList()

    assert list.todo_list == []

def test_todo_added_to_list():
    list = TodoList()
    todo = Todo('Do laundry')

    list.add(todo)

    assert list.todo_list == [todo]

def test_incompleted_todos_shown():
    list = TodoList()
    todo = Todo('Do laundry')
    todo_2 = Todo('Wash up')
    list.add(todo)
    list.add(todo_2)
    
    todo.mark_complete()

    assert list.incomplete() == [todo_2]

def test_completed_todos_shown():
    list = TodoList()
    todo = Todo('Do laundry')
    todo_2 = Todo('Wash up')
    list.add(todo)
    list.add(todo_2)
    
    todo.mark_complete()

    assert list.complete() == [todo]