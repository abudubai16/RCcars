from RCcars import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    steering = db.Column(db.Integer, nullable=False, default=0)
    throttle = db.Column(db.Integer, nullable=False, default=0)
    connection = db.Column(db.Integer, nullable=False, default=0)
    password = db.Column(db.String(60), nullable=False)
    admin = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, password, admin=0):
        self.password = password
        self.admin = admin

    def __repr__(self):
        if self.admin == 0:
            return f"Car {self.id}: Connection {self.connection}, Steering {self.steering}, " \
                   f"Throttle {self.throttle}"
        else:
            return f"User: Admin"
