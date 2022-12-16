""" Security and setting """
from flask import redirect, Blueprint, session, url_for, flash, render_template
from flask_login import set_login_view, fresh_login_required, login_required, current_user
from flask_bcrypt import check_password_hash
from ._tools_ import updateSessionTime
from .accounts import usernames


acc_security = Blueprint("acc_security", __name__)
# security = Blueprint("security", __name__)

# Account security check after logged in
@acc_security.route("/redirect")
@login_required
def securePS_redirect():
    if 'changePS_AfterLogin' in session:
        if session['changePS_AfterLogin'] == "on":
            return redirect(url_for("acc.changePS", user_alias=current_user.alias))
        else:
            return redirect(url_for("features.cake", user_alias=current_user.alias))
    else:
        return redirect(url_for("features.cake", user_alias=current_user.alias))
    
@acc_security.route("/account-security-alert/")
@login_required
def securePS_check():
    if 'changePS_AfterLogin' in session:
        if session['changePS_AfterLogin'] == "on":
            return redirect(url_for("acc.changePS", user_alias=current_user.alias))
        else:
            if (check_password_hash(current_user.password, usernames[current_user.fname])) or (len(session['psw']) <= 7):
                session.pop('psw', None) # clear password stored in cookie
                return render_template("plain.html", user=current_user, title='WARNING!', msg='Your account is at risk, please consider changing your password',warn=True)
        
    return redirect(url_for('acc_security.securePS_redirect'))
