from flask import render_template, Blueprint, request, flash, redirect, url_for, session, abort
from . import systemInfo, systemVersion
from flask_login import login_user, login_required, logout_user, current_user
from flask_bcrypt import check_password_hash
from .models import User
import time

auth = Blueprint('auth', __name__)


@auth.route('/logout/')
@login_required
def logOut():
    logout_user()
    time.sleep(0.2)
    return redirect(url_for('auth.logIn'))

@auth.route('/login/', methods=["POST", "GET"])
def logIn():
    try:
        if User.get_id(current_user):
            return redirect(url_for("features.c", user_id=current_user.id)) # redirect to cake page
    except:
        pass
    if request.method == 'POST' :
        name = request.form.get('fname')
        password = request.form.get('password')
        user = User.query.filter_by(fname=name).first()
        if user :
            if check_password_hash(user.password, password) : # comparing two given parameters
                flash('Logged in Successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Password or the username is incorrect!", category= 'error')
        else:
            flash("Username is incorrect!", category= 'error') 
    
    return render_template('login.html', systemVersion =systemVersion, about=systemInfo, user=current_user)