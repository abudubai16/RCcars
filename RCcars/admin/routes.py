from flask import Blueprint, flash, url_for, redirect, request, render_template
from flask_login import login_user, current_user, login_required
from RCcars.models import User
from RCcars.admin.forms import LoginAdminForm
from RCcars.utils import is_admin
from RCcars.admin.admin_controls import admin_control
from RCcars.player.models import Player
from RCcars import bcrypt

admin = Blueprint('admin', __name__)


@admin.route('/login/admin', methods=['GET', 'POST'])
def login_admin():
    if current_user.get_id() and current_user.admin == 0:
        flash('Access Denied!', 'danger')
        return redirect(url_for('main.home'))
    form = LoginAdminForm()
    if form.validate_on_submit():
        user = User.query.filter_by(admin=1).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            user.admin = 1
            login_user(user)

            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin.game_controls'))
        else:
            flash('Login Unsuccessful', 'danger')
            return redirect(url_for('main.home'))

    return render_template('login_admin.html', title='Login', form=form)


@login_required
@admin.route('/admin/controls', methods=['GET', 'POST'])
def game_controls():
    if not is_admin(current_user):
        return redirect(url_for('login_admin'))

    return render_template('game_control.html', title='Controls', admin_control=admin_control, user=User)


@login_required
@admin.route('/admin/database', methods=['GET', 'POST'])
def database():
    if not is_admin(current_user):
        return redirect(url_for('login_admin'))
    return render_template('database.html', title='Database', user=User, player=Player)

