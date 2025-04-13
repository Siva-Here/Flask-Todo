from models.todo_model import Todo, db

class TodoService:
    @staticmethod
    def get_all_todos(user_id):
        return Todo.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def get_todo_by_id(todo_id, user_id):
        return Todo.query.filter_by(id=todo_id, user_id=user_id).first()

    @staticmethod
    def create_todo(title, user_id):
        todo = Todo(title=title, user_id=user_id)
        db.session.add(todo)
        db.session.commit()
        return todo

    @staticmethod
    def update_todo(todo_id, user_id, title, completed):
        todo = TodoService.get_todo_by_id(todo_id, user_id)
        if todo:
            todo.title = title
            todo.completed = completed
            db.session.commit()
        return todo

    @staticmethod
    def delete_todo(todo_id, user_id):
        todo = TodoService.get_todo_by_id(todo_id, user_id)
        if todo:
            db.session.delete(todo)
            db.session.commit()
            return True
        return False