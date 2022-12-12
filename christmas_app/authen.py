from flask import render_template, Blueprint, request, redirect, url_for, session, abort, flash
from flask_login import login_user, login_required, logout_user, current_user, login_fresh
from flask_bcrypt import check_password_hash
# from ._tools_ import flash # import customized flash method (flask)
from .models import User
from .features import checker # import pre-defined account checker method
import time, json
from datetime import datetime, timezone
from ._tools_ import updateSessionTime

auth = Blueprint('auth', __name__)



@auth.route('/logout/')
@login_required
def logOut():
    session.clear()
    logout_user()
    flash('Please login again to access customized surprise present!', category='logout')
    return redirect(url_for('auth.logIn'))

@auth.route('/login/', methods=["POST", "GET"])
def logIn():
    try:
        if (login_fresh() == False): # redirect user to login page if the session is not fresh 
            # (usually logged in and close the browser and access the page again, 
            # user still logged in to the site however might not able to access to the page that requires fresh login) 
            # [need more customization on reauthorization for fresh login require for more fancy work lol]
            pass
        elif User.get_id(current_user): # if the session is fresh and user already logged in
            # flash("logged in", category='info')
            return redirect(url_for("features.cake", user_alias=current_user.alias)) # redirect to cake page
    except:
        pass
    if request.method == 'POST' :
        name = request.form.get('inputUsername').upper()
        password = request.form.get('inputPassword')
        user = User.query.filter_by(fname=name).first()
        changePS_AfterLogin = request.form.get("next")
        if user :
            if check_password_hash(user.password, password) : # comparing two given parameters
                login_user(user, remember=False) # remember = False cause session timeout implemented and this could override timeout session 
                # Otherwise, could be set to true
                session['loginTime'] = datetime.now(tz=timezone.utc)
                flash('Welcome, "' + name +'"!', category='login')
                if changePS_AfterLogin:
                    return redirect(url_for("acc.changePS", user_alias=current_user.alias))
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
    
  