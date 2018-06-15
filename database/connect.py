import os

from flask import Flask
import flask_mongoalchemy as mongoalchemy


app = Flask(__name__)

app.config['MONGOALCHEMY_DATABASE'] = 'room_scheduler'
app.config['MONGOALCHEMY_CONNECTION_STRING'] = os.environ['MONGO_URI']

db = mongoalchemy.MongoAlchemy(app)