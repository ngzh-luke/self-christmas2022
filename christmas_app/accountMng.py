from flask import redirect, render_template, Blueprint, url_for, request
from flask_login import current_user, login_required, fresh_login_required
from ._tools_ import updateSessionTime

account = Blueprint('acc', __name__)

@account.route('/<string:user_alias>/account-management/', methods=["GET"])
@fresh_login_required
def manager(user_alias):
    updateSessionTime()
    return render_template('account.html', user=current_user, auto=False)

@account.route('/<string:user_alias>/account-management/change-password/', methods=['POST','GET'])
@fresh_login_required
def changePS(user_alias):
    updateSessionTime()
    return render_template('account.html', user=current_user, alias=current_user.alias, auto=True)

@account.route('/wanna-change-password/')
@login_required
def redirector():
    return redirect(url_for('acc.changePS', user_alias=current_user.alias))