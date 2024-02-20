from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from RCcars.config import Config
from RCcars.events import socketio

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)

    from .main.routes import main
    from .admin.routes import admin
    from .player.routes import players
    from .cars.routes import car

    app.register_blueprint(main)
    app.register_blueprint(admin)
    app.register_blueprint(players)
    app.register_blueprint(car)

    return app
