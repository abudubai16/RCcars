from flask import Blueprint, render_template
from flask_login import current_user

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    print('Hello')
    return render_template('home.html', title='Home', current_user=current_user)


@main.route('/about')
def about():
    return render_template('about.html', title='About')


@main.route('/rules')
def rules():
    return render_template('rules.html', title="Rules of the game")
