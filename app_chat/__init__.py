from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from flask_socketio import SocketIO

app= Flask(__name__)

socketio = SocketIO(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
csrf = CSRFProtect(app)
db =SQLAlchemy(app)
app.secret_key='qwert'