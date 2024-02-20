from .extensions import socketio
from flask_login import current_user, login_required
from .admin.admin_controls import admin_control
from flask import redirect, url_for
from flask_socketio import emit


@socketio.on("connect")
def handle_connection():
    from .models import User
    user = User.query.get(current_user.id)
    user.connection = 1


@login_required
@socketio.on("player_game")
def handle_player_inputs(data):
    current_user.throttle = data['throttle']
    current_user.steering = data['steering']


@socketio.on("car_inputs")
def handle_car_inputs(image, name):
    print(image, name)
    data = [current_user.throttle, current_user.steering]
    emit(data)


@socketio.on("game_state")
def change_game_state(controls):
    from .utils import is_admin
    if not is_admin(current_user):
        return redirect(url_for('admin.login_admin'))

    admin_control.reset = not controls["reset"]

    emit("admin_controls")


@socketio.on('change_game')
def change_game(controls):
    from .utils import is_admin
    if not is_admin(current_user):
        return redirect(url_for('admin.login_admin'))

    admin_control.start = not controls["start"]

    emit("admin_controls")


@socketio.on('get_db')
def send_db(status):
    if status == 400:
        data = "Hello"
        socketio.emit("receive_db", data)
    else:
        socketio.emit("recieve_db", "Error")
