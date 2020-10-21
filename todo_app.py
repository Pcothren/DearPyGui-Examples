import dearpygui.core as dpg
import dearpygui.simple as sdpg
import uuid


class TodoApp:
    def __init__(self, todos):
        self.todos = todos

    def __render(self, sender, data):
        """Run every frame to update the GUI.

        Updates the table by clearing it and inserting rows with the data.
        """
        dpg.clear_table('Todos')
        for todo in self.todos:
            dpg.add_row('Todos', [todo['id'], todo['content'], todo['done']])

    def __add_todo(self, sender, data):
        """Add a new todo.

        Get the data from the input text, append a new todo to the todos list
        and then clear the text of the input.
        """
        new_todo_content = dpg.get_value('new-todo-title')
        new_todo = {'id': uuid.uuid4().hex, 'content': new_todo_content, 'done': False}
        self.todos.append(new_todo)
        dpg.set_value('new-todo-title', '')

    def __toggle_todo(self, sender, data):
        """Toggle a todo to True of False.

        Get the selected cell of the table (list of [row index, column index])
        and uses the row index to update the todo at that index in the todos
        list. Then, saves the selected row index in the case you would want to
        delete that todo.
        """
        todo_row = dpg.get_table_selections("Todos")
        todo = self.todos[todo_row[0][0]]
        todo['done'] = not todo['done']
        dpg.add_data('selected-todo-index', self.todos.index(todo))
        dpg.set_value('Selected todo:', f"Selected id: {todo['id']}")

    def __remove_todo(self, sender, data):
        """Remove a todo from the todos list based on the selected row."""
        todo_index = dpg.get_data('selected-todo-index')
        self.todos.pop(todo_index)

    def __clear_todos(self, sender, data):
        """Clear all the todos."""
        self.todos = []

    def show(self):
        """Start the gui."""
        with sdpg.window("Main Window"):
            dpg.set_main_window_size(550, 550)
            dpg.set_main_window_resizable(False)
            dpg.set_main_window_title("Dearpygui Todo App")

            dpg.add_text("Todo App")
            dpg.add_text("Add a todo by writing a title and clicking"
                         " the add todo button", bullet=True)
            dpg.add_text("Toggle a todo by clicking on its table row", bullet=True)
            dpg.add_text("Remove a todo by clicking on its table row and clicking"
                         " the remove todo button", bullet=True)
            dpg.add_separator()

            dpg.add_spacing(count=10)
            dpg.add_input_text("New Todo Title", source="new-todo-title")
            dpg.add_button("Add todo", callback=self.__add_todo)
            dpg.add_spacing(count=10)
            dpg.add_separator()

            dpg.add_table('Todos', ['ID', 'Content', 'Done'], height=200, callback=self.__toggle_todo)
            dpg.add_separator()
            dpg.add_text("Selected todo:")
            dpg.add_button("Remove todo", callback=self.__remove_todo)
            dpg.add_button("Clear todos", callback=self.__clear_todos)

            # Render Callback and Start gui
            dpg.set_render_callback(self.__render)
        dpg.start_dearpygui(primary_window="Main Window")


if __name__ == '__main__':
    todos = [
        {'id': uuid.uuid4().hex, 'content': 'Dear', 'done': False},
        {'id': uuid.uuid4().hex, 'content': 'Py', 'done': False},
        {'id': uuid.uuid4().hex, 'content': 'Gui', 'done': True},
    ]

    todo_app = TodoApp(todos)
    todo_app.show()
