from random import randint
from RCcars import db, bcrypt
from .config import Config
from .models import User
from PIL import Image
from flask import current_app
import os.path


def pin_generator(length=6):
    pin = ''
    for _ in range(length):
        pin = pin + str(randint(0, 9))
    return pin


def create_db(app):
    if 'sqlite:///site.db':  # check if this works properly
        app.app_context().push()
        db.create_all()

        for _ in range(Config.num_players):  # create the 5 cars in the database
            hashed_pin = bcrypt.generate_password_hash(pin_generator(Config.pin_length)).decode('utf-8')
            user = User(password=hashed_pin)
            db.session.add(user)

        hashed_pin = bcrypt.generate_password_hash(Config.password).decode('utf-8')
        admin = User(password=hashed_pin, admin=1)
        db.session.add(admin)
        db.session.commit()


def is_admin(current_user):
    if current_user.is_authenticated and current_user.admin == 1:
        return True
    else:
        return False


def save_frame(frame, name="UnknownSource"):
    picture_name = f"{name}.png"
    picture_path = os.path.join(current_app.root_path, 'pictures', picture_name)

    os.remove(picture_path)

    i = Image.open(frame)
    i.save(picture_path)





