import os
from flask_mongoengine import MongoEngine

def init_database_connection(app):
    app.config['MONGODB_SETTINGS'] = {
        'db': os.environ.get('DATABASE_NAME'),
        'host': 'mongodb+srv://' + os.environ.get('HOST') + '/' + os.environ.get('DATABASE_NAME') + '?retryWrites=true&w=majority',
        'username': os.environ.get('DB_USERNAME'),
        'password': os.environ.get('DB_PASSWORD')
    }
    db = MongoEngine()
    db.init_app(app)