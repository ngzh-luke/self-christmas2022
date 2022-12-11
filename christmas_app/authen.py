from flask import render_template, Blueprint, request, redirect, url_for, session, abort, flash
from flask_login import login_user, login_required, logout_user, current_user
from flask_bcrypt import check_password_hash
# from ._tools_ import flash # import customized flash method (flask)
from .models import User
from .features import checker # import pre-defined account checker method
import time, json

auth = Blueprint('auth', __name__)



@auth.route('/logout/')
@login_required
def logOut():
    logout_user()
    flash('Please login again to access customized surprise present!', category='logout')
    return redirect(url_for('auth.logIn'))

@auth.route('/login/', methods=["POST", "GET"])
def logIn():
    try:
        if User.get_id(current_user):
            # flash("logged in", category='info')
            return redirect(url_for("features.cake", user_alias=current_user.alias)) # redirect to cake page
    except:
        pass
    if request.method == 'POST' :
        name = request.form.get('inputUsername').upper()
        password = request.form.get('inputPassword')
        user = User.query.filter_by(fname=name).first()
        if user :
            if check_password_hash(user.password, password) : # comparing two given parameters
                login_user(user, remember=True)
                flash('Welcome, "' + name +'"!', category='login')
                return redirect(url_for("features.cake", user_alias=current_user.alias))
                
            else:
                flash("Password or the username is incorrect!", category= 'error')
        else:
            flash("Username is incorrect! Feel free to check the existing accounts", category= 'error') 
    
    return render_template('login.html',user=current_user)




@auth.route('/check/', methods=["POST"]) # checker integrated to the login page
def check():
    checker()
                
    return redirect(url_for('auth.logIn'))
    # ("None" if account_ is None else account_)
    
  