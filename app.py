from flask import Flask
from flask_cors import CORS  

from models.user_model import db
from config import Config
from routes.user_routes import register_user_routes
from routes.todo_routes import register_todo_routes

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)  

db.init_app(app)

with app.app_context():
    db.create_all()

register_user_routes(app)
register_todo_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
