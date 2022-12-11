from flask import redirect, render_template, Blueprint, url_for, request
from flask_login import current_user, login_required, fresh_login_required

account = Blueprint('acc', __name__)

@account.route('/<string:user_alias>/account-management/', methods=["GET"])
@fresh_login_required
def manager(user_alias):
    return render_template('account.html', user=current_user, auto=False)

@account.route('/<string:user_alias>/account-management/change-password/', methods=['POST','GET'])
@fresh_login_required
def changePS(user_alias):
    return render_template('account.html', user=current_user, alias=current_user.alias, auto=True)

