class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todo_list.append(todo)
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_todos = [todo for todo in self.todo_list if todo.complete is False]
        return incomplete_todos

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_todos = [todo for todo in self.todo_list if todo.complete is True]
        return complete_todos

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self.todo_list:
            todo.mark_complete()