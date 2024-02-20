from flask import redirect, render_template, Blueprint, url_for, flash, request
from flask_login import logout_user, current_user, login_required, login_user
from RCcars.player.models import Player
from RCcars.admin.admin_controls import admin_control
from RCcars.player.forms import RegistrationPlayerForm, LoginForm
from RCcars.models import load_user
from RCcars import bcrypt, db


players = Blueprint('players', __name__)


@players.route('/register/player', methods=['GET', 'POST'])
def register():
    if not admin_control.reset:
        flash('The admin did not start a new round, please wait', 'danger')
        return redirect(url_for('main.home'))

    form = RegistrationPlayerForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = load_user(user_id=form.car.data)
        user.password = hashed_password
        player = Player(name=form.username.data, number=form.number.data)
        db.session.add(player)
        db.session.commit()

        flash('You can login for the round!', 'success')
        return redirect(url_for('players.login_player'))

    return render_template('register.html', tiitle='Register', form=form)


@players.route('/login/player', methods=['GET', 'POST'])
def login_player():
    if not admin_control.reset:
        flash('The admin did not start a new round, please wait!', 'danger')
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = load_user(user_id=form.car.data)

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=False)
            current_user.connection = 1

            next_page = request.args.get('next')

            flash('Logged in successfully, you can play now!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful', 'danger')
            return redirect(url_for('main.home'))

    return render_template('login.html', title='Login', form=form)


@players.route("/play_game")
def play_game():
    return render_template("play_game.html", title="Play Game")


@login_required
@players.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
