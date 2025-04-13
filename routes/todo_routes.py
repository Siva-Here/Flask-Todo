from views.todo_api import TodoAPI, TodoDetailAPI

def register_todo_routes(app):
    app.add_url_rule('/todos', view_func=TodoAPI.as_view('todos'))
    app.add_url_rule('/todos/<int:todo_id>', view_func=TodoDetailAPI.as_view('todo_detail'))