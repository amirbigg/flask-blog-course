from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'f6a6ec1916a64e3294f4bf45bf183f81'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../blog.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please login first'
login_manager.login_message_category = 'info'

from blog import routes