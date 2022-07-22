from flask import Flask
from flask_mongoengine import MongoEngine
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'jamma',
    'host': '127.0.0.1',
    'port': 27017,
    'username': 'lonewanderer27',
    'password': 'k0yk0y503'
}
db = MongoEngine()
db.init_app(app)
from jamma import routes
