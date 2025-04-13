from flask.views import MethodView
from flask import request, jsonify
from services.todo_service import TodoService
from utils.jwt_helper import token_required

class TodoAPI(MethodView):
    @token_required
    def get(current_user_id, self):
        todos = TodoService.get_all_todos(current_user_id)
        return jsonify([{'id': t.id, 'title': t.title, 'completed': t.completed} for t in todos])

    @token_required
    def post(current_user_id, self):
        data = request.get_json()
        todo = TodoService.create_todo(data['title'], current_user_id)
        return jsonify({'id': todo.id, 'title': todo.title}), 201

class TodoDetailAPI(MethodView):
    @token_required
    def get(current_user_id, self, todo_id):
        todo = TodoService.get_todo_by_id(todo_id, current_user_id)
        if not todo:
            return jsonify({'message': 'Todo not found'}), 404
        return jsonify({
            'id': todo.id,
            'title': todo.title,
            'completed': todo.completed,
            'user_id': todo.user_id
        })

    @token_required
    def put(current_user_id, self, todo_id):
        data = request.get_json()
        todo = TodoService.update_todo(todo_id, current_user_id, data['title'], data['completed'])
        if not todo:
            return jsonify({'message': 'Todo not found'}), 404
        return jsonify({'message': 'Todo updated'})

    @token_required
    def delete(current_user_id, self, todo_id):
        success = TodoService.delete_todo(todo_id, current_user_id)
        if not success:
            return jsonify({'message': 'Todo not found'}), 404
        return jsonify({'message': 'Todo deleted'})

    