from lib.task_checker import *

def test_todo_word_with_symbol():
    check_if_task('#TODO: Laundry') == True

def test_no_todo_word_with_symbol():
    check_if_task('Do Laundry') == False

def test_lowercase_todo_word_with_symbol():
    check_if_task('#todo Laundry') == True

def test_todo_word_without_symbol():
    check_if_task('todo Laundry') == False