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
    
@acc_security.route("/")
@login_required
def securePS_check():
    
    if check_password_hash(current_user.password, usernames[current_user.fname]):
        return render_template("warning.html", user=current_user)
        
    return redirect(url_for('acc_security.securePS_redirect'))
    