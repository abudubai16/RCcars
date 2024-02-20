from flask import Blueprint, request
from RCcars.models import load_user
import fileinput
import json

car = Blueprint('car', __name__)


@car.route('/car/<int:car_id>')
def video_input(car_id):
    pass


@car.route('/car/<int:car_id>')
def car_controls(car_id):

    current_car = load_user(car_id)
    car_inputs = {
        'throttle': current_car.throttle,
        'steering': current_car.steering
    }
    car_json = json.dumps(car_inputs)

