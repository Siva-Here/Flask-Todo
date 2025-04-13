from views.user_api import UserAPI, AuthAPI

def register_user_routes(app):
    app.add_url_rule('/register', view_func=UserAPI.as_view('register'))
    app.add_url_rule('/login', view_func=AuthAPI.as_view('login'))