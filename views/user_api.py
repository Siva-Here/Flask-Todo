from flask.views import MethodView
from flask import request, jsonify
from services.user_service import UserService
from utils.jwt_helper import generate_token

class UserAPI(MethodView):
    def post(self):
        data = request.get_json()
        user = UserService.create_user(data['username'], data['password'])
        if not user:
            return jsonify({'message': 'User already exists'}), 400
        return jsonify({'message': 'User created'}), 201

    def get(self):
        users = UserService.get_all_users()
        return jsonify([{'id': u.id, 'username': u.username} for u in users])

class AuthAPI(MethodView):
    def post(self):
        data = request.get_json()
        user = UserService.authenticate(data['username'], data['password'])
        if not user:
            return jsonify({'message': 'Invalid credentials'}), 401
        token = generate_token(user.id)
        return jsonify({'token': token})