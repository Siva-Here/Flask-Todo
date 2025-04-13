import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'super-secret-key')
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:2KDMKtF5eC7yO9ZPOPepACDlnAk1EI6r@dpg-cvsfbjk9c44c73a1e6l0-a.oregon-postgres.render.com/test_6qhz'
    SQLALCHEMY_TRACK_MODIFICATIONS = False